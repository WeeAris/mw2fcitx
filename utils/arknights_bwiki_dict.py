from mw2fcitx.tweaks.moegirl import tweaks

exports = {
    "source": {
        "api_path": "https://wiki.biligame.com/arknights/api.php",
        "file_path": [],
        "kwargs": {
            "output": "arknights_titles.txt"
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
            "output": "arknights.dict.yaml"
        }
    }, {
        "use": "pinyin",
        "kwargs": {
            "output": "arknights.dict"
        }
    }]
}
