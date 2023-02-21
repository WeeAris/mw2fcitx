from mw2fcitx.tweaks.moegirl import tweaks

exports = {
    "source": {
        "api_path": "https://ff14.huijiwiki.com/api.php",
        "file_path": [],
        "kwargs": {
            "output": "ff14_titles.txt"
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
            "output": "ff14.dict.yaml"
        }
    }, {
        "use": "pinyin",
        "kwargs": {
            "output": "ff14.dict"
        }
    }]
}
