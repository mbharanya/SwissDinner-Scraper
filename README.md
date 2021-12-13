# SwissDinner Scraper
```bash
usage: scraper.py [-h] [--url URL] [--sitemap SITEMAP]


  _________       .__              ________  .__
 /   _____/_  _  _|__| ______ _____\______ \ |__| ____   ____   ___________
 \_____  \\ \/ \/ /  |/  ___//  ___/|    |  \|  |/    \ /    \_/ __ \_  __ \
 /        \\     /|  |\___ \ \___ \ |    `   \  |   |  \   |  \  ___/|  | \/
/_______  / \/\_/ |__/____  >____  >_______  /__|___|  /___|  /\___  >__|
        \/                \/     \/        \/        \/     \/     \/

        Download SwissDinner Episodes

optional arguments:
  -h, --help         show this help message and exit
  --url URL          Direct url to crawl e.g. https://www.telezueri.ch/swissdinner/swissdinner-spezial-mit-
                     michael-imfeld-51-141932031
  --sitemap SITEMAP  Sitemap to crawl
```

## Run
```bash
# download all from sitemap to current dir, skipping already existing ones
docker run --rm -v $(pwd):/output mbharanya/swissdinner
# download specific episode to current dir 
docker run --rm -v $(pwd):/output mbharanya/swissdinner --url https://www.telezueri.ch/swissdinner/swissdinner-spezial-mit-michael-imfeld-51-14193203
```

Files will be downloaded with the episode date and if available the title (older episodes do not have a title). Example: `2016-05-21-Heute kocht Emira (31).mp4`