from mw2fcitx.tweaks.moegirl import tweaks

exports = {
    "source": {
        "api_path": "https://wiki.biligame.com/umamusume/api.php",
        "file_path": [],
        "kwargs": {
            "output": "umamusume_titles.txt"
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
            "output": "umamusume.dict.yaml"
        }
    }, {
        "use": "pinyin",
        "kwargs": {
            "output": "umamusume.dict"
        }
    }]
}
