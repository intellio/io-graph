from __future__ import annotations
from enum import StrEnum


class SecurityReceiverProtocol(StrEnum):
	ftp = "ftp"
	ftps = "ftps"
	syslogUdp = "syslogUdp"
	syslogTcp = "syslogTcp"
	syslogTls = "syslogTls"
	unknownFutureValue = "unknownFutureValue"

