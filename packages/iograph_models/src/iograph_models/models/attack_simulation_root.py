from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AttackSimulationRoot(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	endUserNotifications: list[EndUserNotification] = Field(alias="endUserNotifications",)
	landingPages: list[LandingPage] = Field(alias="landingPages",)
	loginPages: list[LoginPage] = Field(alias="loginPages",)
	operations: list[AttackSimulationOperation] = Field(alias="operations",)
	payloads: list[Payload] = Field(alias="payloads",)
	simulationAutomations: list[SimulationAutomation] = Field(alias="simulationAutomations",)
	simulations: list[Simulation] = Field(alias="simulations",)
	trainings: list[Training] = Field(alias="trainings",)

from .end_user_notification import EndUserNotification
from .landing_page import LandingPage
from .login_page import LoginPage
from .attack_simulation_operation import AttackSimulationOperation
from .payload import Payload
from .simulation_automation import SimulationAutomation
from .simulation import Simulation
from .training import Training

