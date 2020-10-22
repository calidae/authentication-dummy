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

## Support

If you encounter any problems with Tryton, please don't hesitate to ask
questions on the Tryton bug tracker, mailing list, wiki or IRC channel:

  http://bugs.tryton.org/
  http://groups.tryton.org/
  http://wiki.tryton.org/
  irc://irc.freenode.net/tryton

## License

See LICENSE

## Copyright

See COPYRIGHT
