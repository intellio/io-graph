from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ReportRoot(BaseModel):
	authenticationMethods: Optional[AuthenticationMethodsRoot] = Field(alias="authenticationMethods", default=None,)
	dailyPrintUsageByPrinter: Optional[list[PrintUsageByPrinter]] = Field(alias="dailyPrintUsageByPrinter", default=None,)
	dailyPrintUsageByUser: Optional[list[PrintUsageByUser]] = Field(alias="dailyPrintUsageByUser", default=None,)
	monthlyPrintUsageByPrinter: Optional[list[PrintUsageByPrinter]] = Field(alias="monthlyPrintUsageByPrinter", default=None,)
	monthlyPrintUsageByUser: Optional[list[PrintUsageByUser]] = Field(alias="monthlyPrintUsageByUser", default=None,)
	partners: Optional[Partners] = Field(alias="partners", default=None,)
	security: Optional[SecurityReportsRoot] = Field(alias="security", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .authentication_methods_root import AuthenticationMethodsRoot
from .print_usage_by_printer import PrintUsageByPrinter
from .print_usage_by_user import PrintUsageByUser
from .partners import Partners
from .security_reports_root import SecurityReportsRoot
