from mw2fcitx.tweaks.moegirl import tweaks

exports = {
    "source": {
        "api_path": "https://llwiki.org/mediawiki/api.php",
        "file_path": [],
        "kwargs": {
            "output": "llwiki_titles.txt"
        }
    },
    "tweaks":
        tweaks,
    "converter": {
        "use": "opencc",
        "kwargs": {}
    },
    "generator": [{
        "use": "rime",
        "kwargs": {
            "output": "llwiki.dict.yaml"
        }
    }, {
        "use": "pinyin",
        "kwargs": {
            "output": "llwiki.dict"
        }
    }]
}
