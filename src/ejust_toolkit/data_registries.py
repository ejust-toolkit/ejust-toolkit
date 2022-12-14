import pooch

mapping_inequality = pooch.create(
    path=pooch.os_cache("ejust-toolkit"),
    base_url="https://dsl.richmond.edu/panorama/redlining/static/downloads/geojson/",
    # The registry specifies the files that can be fetched
    registry={
        "ILChicago1940.geojson": "sha256:1cc4bb1df11f935a75f68b361b26f7be6480ca6544b34b31cd4533e3c2b1837f",
    },
)

chicago_tiles = pooch.create(
    path=pooch.os_cache("ejust-toolkit"),
    base_url="https://s3.amazonaws.com/holc/tiles/IL/",
    registry={
        "ChicagoSection1/1940/ads.zip": "sha256:34c29870628e11d132c6338855830a0889cea1ae4ec2fdf545a04e1d90e4a82f",
        "IL/ChicagoSection1/1940/rectified.zip": "sha256:4e396915f4883ba0614d69dfdcac8b222ca3dc45045257b6b067380c174f01c0",
        "IL/ChicagoSection1Inset/1940/rectified.zip": "sha256:0cd68d75235a4c340f3e5855463c88138eae3f9bf0de116ca6c6d7194d0e660e",
        "IL/SouthChicago/1940/rectified.zip": "sha256:679f1917d44943b76e68cb84ef6c97b73149c6ba2efe3bf835373b6f9678acc7",
    },
)
