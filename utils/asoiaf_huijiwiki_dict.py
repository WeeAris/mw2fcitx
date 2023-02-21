from mw2fcitx.tweaks.moegirl import tweaks

exports = {
    "source": {
        "api_path": "https://asoiaf.huijiwiki.com/api.php",
        "file_path": [],
        "kwargs": {
            "output": "asoiaf_titles.txt"
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
            "output": "asoiaf.dict.yaml"
        }
    }, {
        "use": "pinyin",
        "kwargs": {
            "output": "asoiaf.dict"
        }
    }]
}
