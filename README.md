# Python QRCode Terminal
You can draw QR codes in your terminal by Python:
![Py QrCode](./example/screenshot_2by1.png)

## TODO
- [ ] See [Unicode Block Elements](https://en.wikipedia.org/wiki/Block_Elements) for more compression.

## Install Dependencies
You need install these:
```shell    
yum install -y python-devel zlib-devel libjpeg-turbo-devel
pip install pillow qrcode
```

## Install
Can be installed with pip:
``` shell
pip install qrcode-terminal
```

## Useage

### As Library
```python
import qrcode_terminal
qrcode_terminal.draw('http://www.baidu.com')
```

### In Terminal
``` shell
qrcode-terminal-py -d http://www.baidu.com
echo "http://www.baidu.com" | qrcode-terminal-py
```

### Scaling
Out of the box we use 2 by 1 unicode blocks, you can also opt-in to use a 3 by 2 unicode block to make the QR-code even smaller:

```
import qrcode_terminal
qrcode_terminal.draw('http://www.baidu.com', render=qrcode_terminal.render_3by2)
```

![Py QrCode](./example/screenshot_3by2.png)
