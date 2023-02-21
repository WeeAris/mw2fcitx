from mw2fcitx.tweaks.moegirl import tweaks

exports = {
    "source": {
        "api_path": "https://wiki.biligame.com/ys/api.php",
        "file_path": [],
        "kwargs": {
            "output": "yuanshen_titles.txt"
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
            "output": "yuanshen.dict.yaml"
        }
    }, {
        "use": "pinyin",
        "kwargs": {
            "output": "yuanshen.dict"
        }
    }]
}
