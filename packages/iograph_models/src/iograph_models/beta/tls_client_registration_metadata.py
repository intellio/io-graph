from __future__ import annotations
from enum import StrEnum


class TlsClientRegistrationMetadata(StrEnum):
	tls_client_auth_subject_dn = "tls_client_auth_subject_dn"
	tls_client_auth_san_dns = "tls_client_auth_san_dns"
	tls_client_auth_san_uri = "tls_client_auth_san_uri"
	tls_client_auth_san_ip = "tls_client_auth_san_ip"
	tls_client_auth_san_email = "tls_client_auth_san_email"
	unknownFutureValue = "unknownFutureValue"

