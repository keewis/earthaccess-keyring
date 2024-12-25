from typing import Any, Optional

import keyring
from earthaccess.auth import Auth, System, logger


def monkeypatch(func):
    setattr(Auth, func.__name__, func)


@monkeypatch
def _keyring(self) -> bool:
    credential = keyring.get_credential("earthaccess")
    if credential is None:
        logger.debug("failed to fetch earthaccess creds from the keyring")

        return False

    authenticated = self._get_credentials(credential.username, credential.password)

    if authenticated:
        logger.debug("Using keyring for EDL")
    else:
        logger.debug("Failed to authenticate using the fetched creds")

    return authenticated


@monkeypatch
def login(
    self,
    strategy: str = "netrc",
    persist: bool = False,
    system: Optional[System] = None,
) -> Any:
    """Authenticate with Earthdata login.

    Parameters:
        strategy:
            The authentication method.

            * **"interactive"**: Enter a username and password.
            * **"netrc"**: (default) Retrieve a username and password from ~/.netrc.
            * **"environment"**:
                Retrieve a username and password from $EARTHDATA_USERNAME and $EARTHDATA_PASSWORD.
        persist: Will persist credentials in a `.netrc` file.
        system: the EDL endpoint to log in to Earthdata, defaults to PROD

    Returns:
        An instance of Auth.
    """
    if system is not None:
        self._set_earthdata_system(system)

    if self.authenticated and (system == self.system):
        logger.debug("We are already authenticated with NASA EDL")
        return self

    if strategy == "interactive":
        self._interactive(persist)
    elif strategy == "netrc":
        self._netrc()
    elif strategy == "environment":
        self._environment()
    elif strategy == "keyring":
        self._keyring()

    return self
