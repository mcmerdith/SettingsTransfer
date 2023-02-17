# Settings Transfer Tool

by mcmerdith

## Usage

Configuration locations are managed through various `.json` files

Saved settings are stored in the `saved` directory

### Configuriation files

Settings configurations are stored in `.json` files in the `configs` directory

>Important: The name of the config is the name of the file and are case-insensitive

##### Example

```json
{
	"locations": [
		"~/.config/nvim",
		"~/.vimrc"
	]
}
```

>NeoVim.json

### Update repository settings from this machine

This will overwrite the existing settings in the repository

#### Update all configs

`python3 update.py`

#### Update specific configs

`python3 update.py <config name>...`

### Install repository settings to this machine

This will overwrite the existing settings on your machine

#### Install all configs

`python3 install.py`

#### Install specific configs

`python3 install.py <config name>...`
