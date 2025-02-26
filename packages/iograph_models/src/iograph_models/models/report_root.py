from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ReportRoot(BaseModel):
	authenticationMethods: Optional[AuthenticationMethodsRoot] = Field(default=None,alias="authenticationMethods",)
	dailyPrintUsageByPrinter: list[PrintUsageByPrinter] = Field(alias="dailyPrintUsageByPrinter",)
	dailyPrintUsageByUser: list[PrintUsageByUser] = Field(alias="dailyPrintUsageByUser",)
	monthlyPrintUsageByPrinter: list[PrintUsageByPrinter] = Field(alias="monthlyPrintUsageByPrinter",)
	monthlyPrintUsageByUser: list[PrintUsageByUser] = Field(alias="monthlyPrintUsageByUser",)
	partners: Optional[Partners] = Field(default=None,alias="partners",)
	security: Optional[SecurityReportsRoot] = Field(default=None,alias="security",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .authentication_methods_root import AuthenticationMethodsRoot
from .print_usage_by_printer import PrintUsageByPrinter
from .print_usage_by_user import PrintUsageByUser
from .print_usage_by_printer import PrintUsageByPrinter
from .print_usage_by_user import PrintUsageByUser
from .partners import Partners
from .security_reports_root import SecurityReportsRoot

