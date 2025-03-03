from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ReportRoot(BaseModel):
	authenticationMethods: Optional[AuthenticationMethodsRoot] = Field(default=None,alias="authenticationMethods",)
	dailyPrintUsageByPrinter: Optional[list[PrintUsageByPrinter]] = Field(default=None,alias="dailyPrintUsageByPrinter",)
	dailyPrintUsageByUser: Optional[list[PrintUsageByUser]] = Field(default=None,alias="dailyPrintUsageByUser",)
	monthlyPrintUsageByPrinter: Optional[list[PrintUsageByPrinter]] = Field(default=None,alias="monthlyPrintUsageByPrinter",)
	monthlyPrintUsageByUser: Optional[list[PrintUsageByUser]] = Field(default=None,alias="monthlyPrintUsageByUser",)
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

