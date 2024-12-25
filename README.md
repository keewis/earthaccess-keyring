# earthaccess-keyring

Allow using a keyring / password manager to provide credentials to `earthaccess.login` by asking the `keyring` to find the `earthaccess` service.

Usage:

```python
import earthaccess
import earthaccess_keyring  # monkeypatches `Auth` to support `strategy="keyring"`

earthaccess.login(strategy="keyring")
```

For this to work, the active keyring needs to expose a `"earthaccess"` service – how this looks depends on the keyring.

For `keepassxc`, for example, configure the secret service integration to export a entry that has the `service` and `username` attributes (since the standard username is exported as the `UserName` secret service attribute).
