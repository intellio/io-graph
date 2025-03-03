from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AttackSimulationRoot(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	endUserNotifications: Optional[list[EndUserNotification]] = Field(default=None,alias="endUserNotifications",)
	landingPages: Optional[list[LandingPage]] = Field(default=None,alias="landingPages",)
	loginPages: Optional[list[LoginPage]] = Field(default=None,alias="loginPages",)
	operations: Optional[list[AttackSimulationOperation]] = Field(default=None,alias="operations",)
	payloads: Optional[list[Payload]] = Field(default=None,alias="payloads",)
	simulationAutomations: Optional[list[SimulationAutomation]] = Field(default=None,alias="simulationAutomations",)
	simulations: Optional[list[Simulation]] = Field(default=None,alias="simulations",)
	trainings: Optional[list[Training]] = Field(default=None,alias="trainings",)

from .end_user_notification import EndUserNotification
from .landing_page import LandingPage
from .login_page import LoginPage
from .attack_simulation_operation import AttackSimulationOperation
from .payload import Payload
from .simulation_automation import SimulationAutomation
from .simulation import Simulation
from .training import Training

