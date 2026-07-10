# Random Ideapad (plz ignore)

so the docker idea is to have a dynamically generated docker image based on predetermined compose templates from different registries. Its randomly generated, by topic or completely random depending on user preference.

Some extensions that could be added on top of this idea are:

- A web interface that displays logs from the vulnerable container, showing whether their attempts are loud, or quiet. Could add a seperate difficulty or scoring system for less noisey attacks, or more complex ones.

- Since a local AI instance is going to be used for the hint and generation system, the user could have the option to just...pen test the AI instance itself. Much further down the line for complete integration, but people will try anyway. Might as well make it part of the experience.


## Update on Ideas

I have the stupidest idea to instead make preset campaigns with the rng being the basis. Implementation is to easy with docker-compose :D. So that would require


- A fake company with a fake website, and mapped docker bridge routing on spin up. So technically that would have to be the backbone.
