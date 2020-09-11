# i3blocks-stocks
An [i3blocks](https://github.com/vivien/i3blocks) implementation for stock visualizing.

![stock-picture](https://i.imgur.com/balCQxs.png)

## Requirements
- [Python3](https://www.python.org/)
- [i3](https://i3wm.org/)
- [i3blocks](https://github.com/vivien/i3blocks)

## Installation
**1.- Clone the git repository and move the folder to i3blocks**
```
git clone https://github.com/Nexobeta28/i3blocks-stocks
mv i3blocks-stocks/stocks .config/i3blocks
rm -rf i3blocks-stocks
```

**2.- Add the block to your config**
Open `~/.config/i3blocks/config` with your favourite text editor and add the following block:

```
[STOCKS]
command=python ~/.config/i3blocks/stocks/get-stock.py
interval=3600
color=#00ff08
```

**3.- Reload i3**
Sign-out, reboot, or press `$mod+shift+r`

*Note: The block won't show until you add the configuration*

## Configuration

All the configurations are in `~/.config/i3blocks/stocks/get_stock.py`

- `API_KEY`: Get you API key [here](https://www.alphavantage.co/support/#api-key) and paste-it
- `SYMBOL`: Set the symbol of the stock that you want to visualize. *(TSLA, AMAZN, BA, ...)*
