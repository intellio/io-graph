from __future__ import annotations
from enum import StrEnum


class KeyStorageProviderOption(StrEnum):
	useTpmKspOtherwiseUseSoftwareKsp = "useTpmKspOtherwiseUseSoftwareKsp"
	useTpmKspOtherwiseFail = "useTpmKspOtherwiseFail"
	usePassportForWorkKspOtherwiseFail = "usePassportForWorkKspOtherwiseFail"
	useSoftwareKsp = "useSoftwareKsp"

