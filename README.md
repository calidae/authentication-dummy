# Authentication Dummy

Authentication dummy is a module developed to work with [Tryton ERP](https://www.tryton.org/).
This module allow to login tryton without password in order to make work easier in development mode.

## How does it work?

Authentication dummy is very simple:
1. Add this module to your dependencies.
2. Set authentication dummy in sessions section in your tryton config file.

```bash
[session]
authentications = dummy
```
