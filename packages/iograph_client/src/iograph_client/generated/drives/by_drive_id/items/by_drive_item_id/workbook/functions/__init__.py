# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .z__test import Z_TestRequest
	from .yield_mat import YieldMatRequest
	from .yield_disc import YieldDiscRequest
	from .yield import YieldRequest
	from .year_frac import YearFracRequest
	from .year import YearRequest
	from .xor import XorRequest
	from .xnpv import XnpvRequest
	from .xirr import XirrRequest
	from .work_day__intl import WorkDay_IntlRequest
	from .work_day import WorkDayRequest
	from .weibull__dist import Weibull_DistRequest
	from .week_num import WeekNumRequest
	from .weekday import WeekdayRequest
	from .vlookup import VlookupRequest
	from .vdb import VdbRequest
	from .var_p_a import VarPARequest
	from .var_a import VarARequest
	from .var__s import Var_SRequest
	from .var__p import Var_PRequest
	from .value import ValueRequest
	from .usdollar import UsdollarRequest
	from .upper import UpperRequest
	from .unicode import UnicodeRequest
	from .unichar import UnicharRequest
	from .type import TypeRequest
	from .trunc import TruncRequest
	from .true import TrueRequest
	from .trim_mean import TrimMeanRequest
	from .trim import TrimRequest
	from .today import TodayRequest
	from .timevalue import TimevalueRequest
	from .time import TimeRequest
	from .text import TextRequest
	from .tbill_yield import TbillYieldRequest
	from .tbill_price import TbillPriceRequest
	from .tbill_eq import TbillEqRequest
	from .tanh import TanhRequest
	from .tan import TanRequest
	from .t__inv_2_t import T_Inv_2TRequest
	from .t__inv import T_InvRequest
	from .t__dist__r_t import T_Dist_RTRequest
	from .t__dist_2_t import T_Dist_2TRequest
	from .t__dist import T_DistRequest
	from .t import TRequest
	from .syd import SydRequest
	from .sum_sq import SumSqRequest
	from .sum_ifs import SumIfsRequest
	from .sum_if import SumIfRequest
	from .sum import SumRequest
	from .subtotal import SubtotalRequest
	from .substitute import SubstituteRequest
	from .st_dev_p_a import StDevPARequest
	from .st_dev_a import StDevARequest
	from .st_dev__s import StDev_SRequest
	from .st_dev__p import StDev_PRequest
	from .standardize import StandardizeRequest
	from .sqrt_pi import SqrtPiRequest
	from .sqrt import SqrtRequest
	from .small import SmallRequest
	from .sln import SlnRequest
	from .skew_p import Skew_pRequest
	from .skew import SkewRequest
	from .sinh import SinhRequest
	from .sin import SinRequest
	from .sign import SignRequest
	from .sheets import SheetsRequest
	from .sheet import SheetRequest
	from .series_sum import SeriesSumRequest
	from .second import SecondRequest
	from .sech import SechRequest
	from .sec import SecRequest
	from .rri import RriRequest
	from .rows import RowsRequest
	from .round_up import RoundUpRequest
	from .round_down import RoundDownRequest
	from .round import RoundRequest
	from .roman import RomanRequest
	from .rightb import RightbRequest
	from .right import RightRequest
	from .rept import ReptRequest
	from .replace_b import ReplaceBRequest
	from .replace import ReplaceRequest
	from .received import ReceivedRequest
	from .rate import RateRequest
	from .rank__eq import Rank_EqRequest
	from .rank__avg import Rank_AvgRequest
	from .rand_between import RandBetweenRequest
	from .rand import RandRequest
	from .radians import RadiansRequest
	from .quotient import QuotientRequest
	from .quartile__inc import Quartile_IncRequest
	from .quartile__exc import Quartile_ExcRequest
	from .pv import PvRequest
	from .proper import ProperRequest
	from .product import ProductRequest
	from .price_mat import PriceMatRequest
	from .price_disc import PriceDiscRequest
	from .price import PriceRequest
	from .ppmt import PpmtRequest
	from .power import PowerRequest
	from .poisson__dist import Poisson_DistRequest
	from .pmt import PmtRequest
	from .pi import PiRequest
	from .phi import PhiRequest
	from .permutationa import PermutationaRequest
	from .permut import PermutRequest
	from .percent_rank__inc import PercentRank_IncRequest
	from .percent_rank__exc import PercentRank_ExcRequest
	from .percentile__inc import Percentile_IncRequest
	from .percentile__exc import Percentile_ExcRequest
	from .pduration import PdurationRequest
	from .or import OrRequest
	from .odd_l_yield import OddLYieldRequest
	from .odd_l_price import OddLPriceRequest
	from .odd_f_yield import OddFYieldRequest
	from .odd_f_price import OddFPriceRequest
	from .odd import OddRequest
	from .oct2_hex import Oct2HexRequest
	from .oct2_dec import Oct2DecRequest
	from .oct2_bin import Oct2BinRequest
	from .number_value import NumberValueRequest
	from .npv import NpvRequest
	from .nper import NperRequest
	from .now import NowRequest
	from .not import NotRequest
	from .norm__s__inv import Norm_S_InvRequest
	from .norm__s__dist import Norm_S_DistRequest
	from .norm__inv import Norm_InvRequest
	from .norm__dist import Norm_DistRequest
	from .nominal import NominalRequest
	from .network_days__intl import NetworkDays_IntlRequest
	from .network_days import NetworkDaysRequest
	from .neg_binom__dist import NegBinom_DistRequest
	from .na import NaRequest
	from .n import NRequest
	from .multi_nomial import MultiNomialRequest
	from .mround import MroundRequest
	from .month import MonthRequest
	from .mod import ModRequest
	from .mirr import MirrRequest
	from .minute import MinuteRequest
	from .min_a import MinARequest
	from .min import MinRequest
	from .midb import MidbRequest
	from .mid import MidRequest
	from .median import MedianRequest
	from .mduration import MdurationRequest
	from .max_a import MaxARequest
	from .max import MaxRequest
	from .match import MatchRequest
	from .lower import LowerRequest
	from .lookup import LookupRequest
	from .log_norm__inv import LogNorm_InvRequest
	from .log_norm__dist import LogNorm_DistRequest
	from .log10 import Log10Request
	from .log import LogRequest
	from .ln import LnRequest
	from .lenb import LenbRequest
	from .len import LenRequest
	from .leftb import LeftbRequest
	from .left import LeftRequest
	from .lcm import LcmRequest
	from .large import LargeRequest
	from .kurt import KurtRequest
	from .is_text import IsTextRequest
	from .isref import IsrefRequest
	from .ispmt import IspmtRequest
	from .iso_week_num import IsoWeekNumRequest
	from .is_odd import IsOddRequest
	from .iso__ceiling import Iso_CeilingRequest
	from .is_number import IsNumberRequest
	from .is_non_text import IsNonTextRequest
	from .is_n_a import IsNARequest
	from .is_logical import IsLogicalRequest
	from .is_formula import IsFormulaRequest
	from .is_even import IsEvenRequest
	from .is_error import IsErrorRequest
	from .is_err import IsErrRequest
	from .irr import IrrRequest
	from .ipmt import IpmtRequest
	from .int_rate import IntRateRequest
	from .int import IntRequest
	from .im_tan import ImTanRequest
	from .im_sum import ImSumRequest
	from .im_sub import ImSubRequest
	from .im_sqrt import ImSqrtRequest
	from .im_sinh import ImSinhRequest
	from .im_sin import ImSinRequest
	from .im_sech import ImSechRequest
	from .im_sec import ImSecRequest
	from .im_real import ImRealRequest
	from .im_product import ImProductRequest
	from .im_power import ImPowerRequest
	from .im_log2 import ImLog2Request
	from .im_log10 import ImLog10Request
	from .im_ln import ImLnRequest
	from .im_exp import ImExpRequest
	from .im_div import ImDivRequest
	from .im_csch import ImCschRequest
	from .im_csc import ImCscRequest
	from .im_cot import ImCotRequest
	from .im_cosh import ImCoshRequest
	from .im_cos import ImCosRequest
	from .im_conjugate import ImConjugateRequest
	from .im_argument import ImArgumentRequest
	from .imaginary import ImaginaryRequest
	from .im_abs import ImAbsRequest
	from .if import IfRequest
	from .hyp_geom__dist import HypGeom_DistRequest
	from .hyperlink import HyperlinkRequest
	from .hour import HourRequest
	from .hlookup import HlookupRequest
	from .hex2_oct import Hex2OctRequest
	from .hex2_dec import Hex2DecRequest
	from .hex2_bin import Hex2BinRequest
	from .har_mean import HarMeanRequest
	from .ge_step import GeStepRequest
	from .geo_mean import GeoMeanRequest
	from .gcd import GcdRequest
	from .gauss import GaussRequest
	from .gamma_ln__precise import GammaLn_PreciseRequest
	from .gamma_ln import GammaLnRequest
	from .gamma__inv import Gamma_InvRequest
	from .gamma__dist import Gamma_DistRequest
	from .gamma import GammaRequest
	from .fvschedule import FvscheduleRequest
	from .fv import FvRequest
	from .floor__precise import Floor_PreciseRequest
	from .floor__math import Floor_MathRequest
	from .fixed import FixedRequest
	from .fisher_inv import FisherInvRequest
	from .fisher import FisherRequest
	from .find_b import FindBRequest
	from .find import FindRequest
	from .false import FalseRequest
	from .fact_double import FactDoubleRequest
	from .fact import FactRequest
	from .f__inv__r_t import F_Inv_RTRequest
	from .f__inv import F_InvRequest
	from .f__dist__r_t import F_Dist_RTRequest
	from .f__dist import F_DistRequest
	from .expon__dist import Expon_DistRequest
	from .exp import ExpRequest
	from .exact import ExactRequest
	from .even import EvenRequest
	from .error__type import Error_TypeRequest
	from .erf_c__precise import ErfC_PreciseRequest
	from .erf_c import ErfCRequest
	from .erf__precise import Erf_PreciseRequest
	from .erf import ErfRequest
	from .eo_month import EoMonthRequest
	from .effect import EffectRequest
	from .edate import EdateRequest
	from .ecma__ceiling import Ecma_CeilingRequest
	from .dvar_p import DvarPRequest
	from .dvar import DvarRequest
	from .duration import DurationRequest
	from .dsum import DsumRequest
	from .dst_dev_p import DstDevPRequest
	from .dst_dev import DstDevRequest
	from .dproduct import DproductRequest
	from .dollar_fr import DollarFrRequest
	from .dollar_de import DollarDeRequest
	from .dollar import DollarRequest
	from .dmin import DminRequest
	from .dmax import DmaxRequest
	from .disc import DiscRequest
	from .dget import DgetRequest
	from .dev_sq import DevSqRequest
	from .delta import DeltaRequest
	from .degrees import DegreesRequest
	from .decimal import DecimalRequest
	from .dec2_oct import Dec2OctRequest
	from .dec2_hex import Dec2HexRequest
	from .dec2_bin import Dec2BinRequest
	from .ddb import DdbRequest
	from .dcount_a import DcountARequest
	from .dcount import DcountRequest
	from .dbcs import DbcsRequest
	from .db import DbRequest
	from .days360 import Days360Request
	from .days import DaysRequest
	from .day import DayRequest
	from .daverage import DaverageRequest
	from .datevalue import DatevalueRequest
	from .date import DateRequest
	from .cum_princ import CumPrincRequest
	from .cum_i_pmt import CumIPmtRequest
	from .csch import CschRequest
	from .csc import CscRequest
	from .coup_pcd import CoupPcdRequest
	from .coup_num import CoupNumRequest
	from .coup_ncd import CoupNcdRequest
	from .coup_days_nc import CoupDaysNcRequest
	from .coup_days import CoupDaysRequest
	from .coup_day_bs import CoupDayBsRequest
	from .count_ifs import CountIfsRequest
	from .count_if import CountIfRequest
	from .count_blank import CountBlankRequest
	from .count_a import CountARequest
	from .count import CountRequest
	from .coth import CothRequest
	from .cot import CotRequest
	from .cosh import CoshRequest
	from .cos import CosRequest
	from .convert import ConvertRequest
	from .confidence__t import Confidence_TRequest
	from .confidence__norm import Confidence_NormRequest
	from .concatenate import ConcatenateRequest
	from .complex import ComplexRequest
	from .combina import CombinaRequest
	from .combin import CombinRequest
	from .columns import ColumnsRequest
	from .code import CodeRequest
	from .clean import CleanRequest
	from .choose import ChooseRequest
	from .chi_sq__inv__r_t import ChiSq_Inv_RTRequest
	from .chi_sq__inv import ChiSq_InvRequest
	from .chi_sq__dist__r_t import ChiSq_Dist_RTRequest
	from .chi_sq__dist import ChiSq_DistRequest
	from .char import CharRequest
	from .ceiling__precise import Ceiling_PreciseRequest
	from .ceiling__math import Ceiling_MathRequest
	from .bitxor import BitxorRequest
	from .bitrshift import BitrshiftRequest
	from .bitor import BitorRequest
	from .bitlshift import BitlshiftRequest
	from .bitand import BitandRequest
	from .binom__inv import Binom_InvRequest
	from .binom__dist__range import Binom_Dist_RangeRequest
	from .binom__dist import Binom_DistRequest
	from .bin2_oct import Bin2OctRequest
	from .bin2_hex import Bin2HexRequest
	from .bin2_dec import Bin2DecRequest
	from .beta__inv import Beta_InvRequest
	from .beta__dist import Beta_DistRequest
	from .bessel_y import BesselYRequest
	from .bessel_k import BesselKRequest
	from .bessel_j import BesselJRequest
	from .bessel_i import BesselIRequest
	from .base import BaseRequest
	from .baht_text import BahtTextRequest
	from .average_ifs import AverageIfsRequest
	from .average_if import AverageIfRequest
	from .average_a import AverageARequest
	from .average import AverageRequest
	from .ave_dev import AveDevRequest
	from .atanh import AtanhRequest
	from .atan2 import Atan2Request
	from .atan import AtanRequest
	from .asinh import AsinhRequest
	from .asin import AsinRequest
	from .asc import AscRequest
	from .areas import AreasRequest
	from .arabic import ArabicRequest
	from .and import AndRequest
	from .amor_linc import AmorLincRequest
	from .amor_degrc import AmorDegrcRequest
	from .acoth import AcothRequest
	from .acot import AcotRequest
	from .acosh import AcoshRequest
	from .acos import AcosRequest
	from .accr_int_m import AccrIntMRequest
	from .accr_int import AccrIntRequest
	from .abs import AbsRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.workbook_functions import WorkbookFunctions
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class FunctionsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/functions", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WorkbookFunctions:
		"""
		Get functions from drives
		
		"""
		tags = ['drives.driveItem']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.GET,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_async(request_info, WorkbookFunctions, error_mapping)

	async def patch(
		self,
		body: WorkbookFunctions,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WorkbookFunctions:
		"""
		Update the navigation property functions in drives
		
		"""
		tags = ['drives.driveItem']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PATCH,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, WorkbookFunctions, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property functions for drives
		
		"""
		tags = ['drives.driveItem']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag', 'schema': {'type': 'string'}}]

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.DELETE,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")



	def with_url(self, raw_url: str) -> FunctionsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: FunctionsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return FunctionsRequest(self.request_adapter, self.path_parameters)

	def abs(self,
		drive_id: str,
		driveItem_id: str,
	) -> AbsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .abs import AbsRequest
		return AbsRequest(self.request_adapter, path_parameters)

	def accr_int(self,
		drive_id: str,
		driveItem_id: str,
	) -> AccrIntRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .accr_int import AccrIntRequest
		return AccrIntRequest(self.request_adapter, path_parameters)

	def accr_int_m(self,
		drive_id: str,
		driveItem_id: str,
	) -> AccrIntMRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .accr_int_m import AccrIntMRequest
		return AccrIntMRequest(self.request_adapter, path_parameters)

	def acos(self,
		drive_id: str,
		driveItem_id: str,
	) -> AcosRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .acos import AcosRequest
		return AcosRequest(self.request_adapter, path_parameters)

	def acosh(self,
		drive_id: str,
		driveItem_id: str,
	) -> AcoshRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .acosh import AcoshRequest
		return AcoshRequest(self.request_adapter, path_parameters)

	def acot(self,
		drive_id: str,
		driveItem_id: str,
	) -> AcotRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .acot import AcotRequest
		return AcotRequest(self.request_adapter, path_parameters)

	def acoth(self,
		drive_id: str,
		driveItem_id: str,
	) -> AcothRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .acoth import AcothRequest
		return AcothRequest(self.request_adapter, path_parameters)

	def amor_degrc(self,
		drive_id: str,
		driveItem_id: str,
	) -> AmorDegrcRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .amor_degrc import AmorDegrcRequest
		return AmorDegrcRequest(self.request_adapter, path_parameters)

	def amor_linc(self,
		drive_id: str,
		driveItem_id: str,
	) -> AmorLincRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .amor_linc import AmorLincRequest
		return AmorLincRequest(self.request_adapter, path_parameters)

	def and(self,
		drive_id: str,
		driveItem_id: str,
	) -> AndRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .and import AndRequest
		return AndRequest(self.request_adapter, path_parameters)

	def arabic(self,
		drive_id: str,
		driveItem_id: str,
	) -> ArabicRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .arabic import ArabicRequest
		return ArabicRequest(self.request_adapter, path_parameters)

	def areas(self,
		drive_id: str,
		driveItem_id: str,
	) -> AreasRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .areas import AreasRequest
		return AreasRequest(self.request_adapter, path_parameters)

	def asc(self,
		drive_id: str,
		driveItem_id: str,
	) -> AscRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .asc import AscRequest
		return AscRequest(self.request_adapter, path_parameters)

	def asin(self,
		drive_id: str,
		driveItem_id: str,
	) -> AsinRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .asin import AsinRequest
		return AsinRequest(self.request_adapter, path_parameters)

	def asinh(self,
		drive_id: str,
		driveItem_id: str,
	) -> AsinhRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .asinh import AsinhRequest
		return AsinhRequest(self.request_adapter, path_parameters)

	def atan(self,
		drive_id: str,
		driveItem_id: str,
	) -> AtanRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .atan import AtanRequest
		return AtanRequest(self.request_adapter, path_parameters)

	def atan2(self,
		drive_id: str,
		driveItem_id: str,
	) -> Atan2Request:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .atan2 import Atan2Request
		return Atan2Request(self.request_adapter, path_parameters)

	def atanh(self,
		drive_id: str,
		driveItem_id: str,
	) -> AtanhRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .atanh import AtanhRequest
		return AtanhRequest(self.request_adapter, path_parameters)

	def ave_dev(self,
		drive_id: str,
		driveItem_id: str,
	) -> AveDevRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .ave_dev import AveDevRequest
		return AveDevRequest(self.request_adapter, path_parameters)

	def average(self,
		drive_id: str,
		driveItem_id: str,
	) -> AverageRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .average import AverageRequest
		return AverageRequest(self.request_adapter, path_parameters)

	def average_a(self,
		drive_id: str,
		driveItem_id: str,
	) -> AverageARequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .average_a import AverageARequest
		return AverageARequest(self.request_adapter, path_parameters)

	def average_if(self,
		drive_id: str,
		driveItem_id: str,
	) -> AverageIfRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .average_if import AverageIfRequest
		return AverageIfRequest(self.request_adapter, path_parameters)

	def average_ifs(self,
		drive_id: str,
		driveItem_id: str,
	) -> AverageIfsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .average_ifs import AverageIfsRequest
		return AverageIfsRequest(self.request_adapter, path_parameters)

	def baht_text(self,
		drive_id: str,
		driveItem_id: str,
	) -> BahtTextRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .baht_text import BahtTextRequest
		return BahtTextRequest(self.request_adapter, path_parameters)

	def base(self,
		drive_id: str,
		driveItem_id: str,
	) -> BaseRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .base import BaseRequest
		return BaseRequest(self.request_adapter, path_parameters)

	def bessel_i(self,
		drive_id: str,
		driveItem_id: str,
	) -> BesselIRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .bessel_i import BesselIRequest
		return BesselIRequest(self.request_adapter, path_parameters)

	def bessel_j(self,
		drive_id: str,
		driveItem_id: str,
	) -> BesselJRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .bessel_j import BesselJRequest
		return BesselJRequest(self.request_adapter, path_parameters)

	def bessel_k(self,
		drive_id: str,
		driveItem_id: str,
	) -> BesselKRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .bessel_k import BesselKRequest
		return BesselKRequest(self.request_adapter, path_parameters)

	def bessel_y(self,
		drive_id: str,
		driveItem_id: str,
	) -> BesselYRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .bessel_y import BesselYRequest
		return BesselYRequest(self.request_adapter, path_parameters)

	def beta__dist(self,
		drive_id: str,
		driveItem_id: str,
	) -> Beta_DistRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .beta__dist import Beta_DistRequest
		return Beta_DistRequest(self.request_adapter, path_parameters)

	def beta__inv(self,
		drive_id: str,
		driveItem_id: str,
	) -> Beta_InvRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .beta__inv import Beta_InvRequest
		return Beta_InvRequest(self.request_adapter, path_parameters)

	def bin2_dec(self,
		drive_id: str,
		driveItem_id: str,
	) -> Bin2DecRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .bin2_dec import Bin2DecRequest
		return Bin2DecRequest(self.request_adapter, path_parameters)

	def bin2_hex(self,
		drive_id: str,
		driveItem_id: str,
	) -> Bin2HexRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .bin2_hex import Bin2HexRequest
		return Bin2HexRequest(self.request_adapter, path_parameters)

	def bin2_oct(self,
		drive_id: str,
		driveItem_id: str,
	) -> Bin2OctRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .bin2_oct import Bin2OctRequest
		return Bin2OctRequest(self.request_adapter, path_parameters)

	def binom__dist(self,
		drive_id: str,
		driveItem_id: str,
	) -> Binom_DistRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .binom__dist import Binom_DistRequest
		return Binom_DistRequest(self.request_adapter, path_parameters)

	def binom__dist__range(self,
		drive_id: str,
		driveItem_id: str,
	) -> Binom_Dist_RangeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .binom__dist__range import Binom_Dist_RangeRequest
		return Binom_Dist_RangeRequest(self.request_adapter, path_parameters)

	def binom__inv(self,
		drive_id: str,
		driveItem_id: str,
	) -> Binom_InvRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .binom__inv import Binom_InvRequest
		return Binom_InvRequest(self.request_adapter, path_parameters)

	def bitand(self,
		drive_id: str,
		driveItem_id: str,
	) -> BitandRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .bitand import BitandRequest
		return BitandRequest(self.request_adapter, path_parameters)

	def bitlshift(self,
		drive_id: str,
		driveItem_id: str,
	) -> BitlshiftRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .bitlshift import BitlshiftRequest
		return BitlshiftRequest(self.request_adapter, path_parameters)

	def bitor(self,
		drive_id: str,
		driveItem_id: str,
	) -> BitorRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .bitor import BitorRequest
		return BitorRequest(self.request_adapter, path_parameters)

	def bitrshift(self,
		drive_id: str,
		driveItem_id: str,
	) -> BitrshiftRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .bitrshift import BitrshiftRequest
		return BitrshiftRequest(self.request_adapter, path_parameters)

	def bitxor(self,
		drive_id: str,
		driveItem_id: str,
	) -> BitxorRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .bitxor import BitxorRequest
		return BitxorRequest(self.request_adapter, path_parameters)

	def ceiling__math(self,
		drive_id: str,
		driveItem_id: str,
	) -> Ceiling_MathRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .ceiling__math import Ceiling_MathRequest
		return Ceiling_MathRequest(self.request_adapter, path_parameters)

	def ceiling__precise(self,
		drive_id: str,
		driveItem_id: str,
	) -> Ceiling_PreciseRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .ceiling__precise import Ceiling_PreciseRequest
		return Ceiling_PreciseRequest(self.request_adapter, path_parameters)

	def char(self,
		drive_id: str,
		driveItem_id: str,
	) -> CharRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .char import CharRequest
		return CharRequest(self.request_adapter, path_parameters)

	def chi_sq__dist(self,
		drive_id: str,
		driveItem_id: str,
	) -> ChiSq_DistRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .chi_sq__dist import ChiSq_DistRequest
		return ChiSq_DistRequest(self.request_adapter, path_parameters)

	def chi_sq__dist__r_t(self,
		drive_id: str,
		driveItem_id: str,
	) -> ChiSq_Dist_RTRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .chi_sq__dist__r_t import ChiSq_Dist_RTRequest
		return ChiSq_Dist_RTRequest(self.request_adapter, path_parameters)

	def chi_sq__inv(self,
		drive_id: str,
		driveItem_id: str,
	) -> ChiSq_InvRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .chi_sq__inv import ChiSq_InvRequest
		return ChiSq_InvRequest(self.request_adapter, path_parameters)

	def chi_sq__inv__r_t(self,
		drive_id: str,
		driveItem_id: str,
	) -> ChiSq_Inv_RTRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .chi_sq__inv__r_t import ChiSq_Inv_RTRequest
		return ChiSq_Inv_RTRequest(self.request_adapter, path_parameters)

	def choose(self,
		drive_id: str,
		driveItem_id: str,
	) -> ChooseRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .choose import ChooseRequest
		return ChooseRequest(self.request_adapter, path_parameters)

	def clean(self,
		drive_id: str,
		driveItem_id: str,
	) -> CleanRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .clean import CleanRequest
		return CleanRequest(self.request_adapter, path_parameters)

	def code(self,
		drive_id: str,
		driveItem_id: str,
	) -> CodeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .code import CodeRequest
		return CodeRequest(self.request_adapter, path_parameters)

	def columns(self,
		drive_id: str,
		driveItem_id: str,
	) -> ColumnsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .columns import ColumnsRequest
		return ColumnsRequest(self.request_adapter, path_parameters)

	def combin(self,
		drive_id: str,
		driveItem_id: str,
	) -> CombinRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .combin import CombinRequest
		return CombinRequest(self.request_adapter, path_parameters)

	def combina(self,
		drive_id: str,
		driveItem_id: str,
	) -> CombinaRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .combina import CombinaRequest
		return CombinaRequest(self.request_adapter, path_parameters)

	def complex(self,
		drive_id: str,
		driveItem_id: str,
	) -> ComplexRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .complex import ComplexRequest
		return ComplexRequest(self.request_adapter, path_parameters)

	def concatenate(self,
		drive_id: str,
		driveItem_id: str,
	) -> ConcatenateRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .concatenate import ConcatenateRequest
		return ConcatenateRequest(self.request_adapter, path_parameters)

	def confidence__norm(self,
		drive_id: str,
		driveItem_id: str,
	) -> Confidence_NormRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .confidence__norm import Confidence_NormRequest
		return Confidence_NormRequest(self.request_adapter, path_parameters)

	def confidence__t(self,
		drive_id: str,
		driveItem_id: str,
	) -> Confidence_TRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .confidence__t import Confidence_TRequest
		return Confidence_TRequest(self.request_adapter, path_parameters)

	def convert(self,
		drive_id: str,
		driveItem_id: str,
	) -> ConvertRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .convert import ConvertRequest
		return ConvertRequest(self.request_adapter, path_parameters)

	def cos(self,
		drive_id: str,
		driveItem_id: str,
	) -> CosRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .cos import CosRequest
		return CosRequest(self.request_adapter, path_parameters)

	def cosh(self,
		drive_id: str,
		driveItem_id: str,
	) -> CoshRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .cosh import CoshRequest
		return CoshRequest(self.request_adapter, path_parameters)

	def cot(self,
		drive_id: str,
		driveItem_id: str,
	) -> CotRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .cot import CotRequest
		return CotRequest(self.request_adapter, path_parameters)

	def coth(self,
		drive_id: str,
		driveItem_id: str,
	) -> CothRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .coth import CothRequest
		return CothRequest(self.request_adapter, path_parameters)

	def count(self,
		drive_id: str,
		driveItem_id: str,
	) -> CountRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def count_a(self,
		drive_id: str,
		driveItem_id: str,
	) -> CountARequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .count_a import CountARequest
		return CountARequest(self.request_adapter, path_parameters)

	def count_blank(self,
		drive_id: str,
		driveItem_id: str,
	) -> CountBlankRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .count_blank import CountBlankRequest
		return CountBlankRequest(self.request_adapter, path_parameters)

	def count_if(self,
		drive_id: str,
		driveItem_id: str,
	) -> CountIfRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .count_if import CountIfRequest
		return CountIfRequest(self.request_adapter, path_parameters)

	def count_ifs(self,
		drive_id: str,
		driveItem_id: str,
	) -> CountIfsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .count_ifs import CountIfsRequest
		return CountIfsRequest(self.request_adapter, path_parameters)

	def coup_day_bs(self,
		drive_id: str,
		driveItem_id: str,
	) -> CoupDayBsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .coup_day_bs import CoupDayBsRequest
		return CoupDayBsRequest(self.request_adapter, path_parameters)

	def coup_days(self,
		drive_id: str,
		driveItem_id: str,
	) -> CoupDaysRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .coup_days import CoupDaysRequest
		return CoupDaysRequest(self.request_adapter, path_parameters)

	def coup_days_nc(self,
		drive_id: str,
		driveItem_id: str,
	) -> CoupDaysNcRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .coup_days_nc import CoupDaysNcRequest
		return CoupDaysNcRequest(self.request_adapter, path_parameters)

	def coup_ncd(self,
		drive_id: str,
		driveItem_id: str,
	) -> CoupNcdRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .coup_ncd import CoupNcdRequest
		return CoupNcdRequest(self.request_adapter, path_parameters)

	def coup_num(self,
		drive_id: str,
		driveItem_id: str,
	) -> CoupNumRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .coup_num import CoupNumRequest
		return CoupNumRequest(self.request_adapter, path_parameters)

	def coup_pcd(self,
		drive_id: str,
		driveItem_id: str,
	) -> CoupPcdRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .coup_pcd import CoupPcdRequest
		return CoupPcdRequest(self.request_adapter, path_parameters)

	def csc(self,
		drive_id: str,
		driveItem_id: str,
	) -> CscRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .csc import CscRequest
		return CscRequest(self.request_adapter, path_parameters)

	def csch(self,
		drive_id: str,
		driveItem_id: str,
	) -> CschRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .csch import CschRequest
		return CschRequest(self.request_adapter, path_parameters)

	def cum_i_pmt(self,
		drive_id: str,
		driveItem_id: str,
	) -> CumIPmtRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .cum_i_pmt import CumIPmtRequest
		return CumIPmtRequest(self.request_adapter, path_parameters)

	def cum_princ(self,
		drive_id: str,
		driveItem_id: str,
	) -> CumPrincRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .cum_princ import CumPrincRequest
		return CumPrincRequest(self.request_adapter, path_parameters)

	def date(self,
		drive_id: str,
		driveItem_id: str,
	) -> DateRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .date import DateRequest
		return DateRequest(self.request_adapter, path_parameters)

	def datevalue(self,
		drive_id: str,
		driveItem_id: str,
	) -> DatevalueRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .datevalue import DatevalueRequest
		return DatevalueRequest(self.request_adapter, path_parameters)

	def daverage(self,
		drive_id: str,
		driveItem_id: str,
	) -> DaverageRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .daverage import DaverageRequest
		return DaverageRequest(self.request_adapter, path_parameters)

	def day(self,
		drive_id: str,
		driveItem_id: str,
	) -> DayRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .day import DayRequest
		return DayRequest(self.request_adapter, path_parameters)

	def days(self,
		drive_id: str,
		driveItem_id: str,
	) -> DaysRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .days import DaysRequest
		return DaysRequest(self.request_adapter, path_parameters)

	def days360(self,
		drive_id: str,
		driveItem_id: str,
	) -> Days360Request:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .days360 import Days360Request
		return Days360Request(self.request_adapter, path_parameters)

	def db(self,
		drive_id: str,
		driveItem_id: str,
	) -> DbRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .db import DbRequest
		return DbRequest(self.request_adapter, path_parameters)

	def dbcs(self,
		drive_id: str,
		driveItem_id: str,
	) -> DbcsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .dbcs import DbcsRequest
		return DbcsRequest(self.request_adapter, path_parameters)

	def dcount(self,
		drive_id: str,
		driveItem_id: str,
	) -> DcountRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .dcount import DcountRequest
		return DcountRequest(self.request_adapter, path_parameters)

	def dcount_a(self,
		drive_id: str,
		driveItem_id: str,
	) -> DcountARequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .dcount_a import DcountARequest
		return DcountARequest(self.request_adapter, path_parameters)

	def ddb(self,
		drive_id: str,
		driveItem_id: str,
	) -> DdbRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .ddb import DdbRequest
		return DdbRequest(self.request_adapter, path_parameters)

	def dec2_bin(self,
		drive_id: str,
		driveItem_id: str,
	) -> Dec2BinRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .dec2_bin import Dec2BinRequest
		return Dec2BinRequest(self.request_adapter, path_parameters)

	def dec2_hex(self,
		drive_id: str,
		driveItem_id: str,
	) -> Dec2HexRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .dec2_hex import Dec2HexRequest
		return Dec2HexRequest(self.request_adapter, path_parameters)

	def dec2_oct(self,
		drive_id: str,
		driveItem_id: str,
	) -> Dec2OctRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .dec2_oct import Dec2OctRequest
		return Dec2OctRequest(self.request_adapter, path_parameters)

	def decimal(self,
		drive_id: str,
		driveItem_id: str,
	) -> DecimalRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .decimal import DecimalRequest
		return DecimalRequest(self.request_adapter, path_parameters)

	def degrees(self,
		drive_id: str,
		driveItem_id: str,
	) -> DegreesRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .degrees import DegreesRequest
		return DegreesRequest(self.request_adapter, path_parameters)

	def delta(self,
		drive_id: str,
		driveItem_id: str,
	) -> DeltaRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .delta import DeltaRequest
		return DeltaRequest(self.request_adapter, path_parameters)

	def dev_sq(self,
		drive_id: str,
		driveItem_id: str,
	) -> DevSqRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .dev_sq import DevSqRequest
		return DevSqRequest(self.request_adapter, path_parameters)

	def dget(self,
		drive_id: str,
		driveItem_id: str,
	) -> DgetRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .dget import DgetRequest
		return DgetRequest(self.request_adapter, path_parameters)

	def disc(self,
		drive_id: str,
		driveItem_id: str,
	) -> DiscRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .disc import DiscRequest
		return DiscRequest(self.request_adapter, path_parameters)

	def dmax(self,
		drive_id: str,
		driveItem_id: str,
	) -> DmaxRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .dmax import DmaxRequest
		return DmaxRequest(self.request_adapter, path_parameters)

	def dmin(self,
		drive_id: str,
		driveItem_id: str,
	) -> DminRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .dmin import DminRequest
		return DminRequest(self.request_adapter, path_parameters)

	def dollar(self,
		drive_id: str,
		driveItem_id: str,
	) -> DollarRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .dollar import DollarRequest
		return DollarRequest(self.request_adapter, path_parameters)

	def dollar_de(self,
		drive_id: str,
		driveItem_id: str,
	) -> DollarDeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .dollar_de import DollarDeRequest
		return DollarDeRequest(self.request_adapter, path_parameters)

	def dollar_fr(self,
		drive_id: str,
		driveItem_id: str,
	) -> DollarFrRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .dollar_fr import DollarFrRequest
		return DollarFrRequest(self.request_adapter, path_parameters)

	def dproduct(self,
		drive_id: str,
		driveItem_id: str,
	) -> DproductRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .dproduct import DproductRequest
		return DproductRequest(self.request_adapter, path_parameters)

	def dst_dev(self,
		drive_id: str,
		driveItem_id: str,
	) -> DstDevRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .dst_dev import DstDevRequest
		return DstDevRequest(self.request_adapter, path_parameters)

	def dst_dev_p(self,
		drive_id: str,
		driveItem_id: str,
	) -> DstDevPRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .dst_dev_p import DstDevPRequest
		return DstDevPRequest(self.request_adapter, path_parameters)

	def dsum(self,
		drive_id: str,
		driveItem_id: str,
	) -> DsumRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .dsum import DsumRequest
		return DsumRequest(self.request_adapter, path_parameters)

	def duration(self,
		drive_id: str,
		driveItem_id: str,
	) -> DurationRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .duration import DurationRequest
		return DurationRequest(self.request_adapter, path_parameters)

	def dvar(self,
		drive_id: str,
		driveItem_id: str,
	) -> DvarRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .dvar import DvarRequest
		return DvarRequest(self.request_adapter, path_parameters)

	def dvar_p(self,
		drive_id: str,
		driveItem_id: str,
	) -> DvarPRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .dvar_p import DvarPRequest
		return DvarPRequest(self.request_adapter, path_parameters)

	def ecma__ceiling(self,
		drive_id: str,
		driveItem_id: str,
	) -> Ecma_CeilingRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .ecma__ceiling import Ecma_CeilingRequest
		return Ecma_CeilingRequest(self.request_adapter, path_parameters)

	def edate(self,
		drive_id: str,
		driveItem_id: str,
	) -> EdateRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .edate import EdateRequest
		return EdateRequest(self.request_adapter, path_parameters)

	def effect(self,
		drive_id: str,
		driveItem_id: str,
	) -> EffectRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .effect import EffectRequest
		return EffectRequest(self.request_adapter, path_parameters)

	def eo_month(self,
		drive_id: str,
		driveItem_id: str,
	) -> EoMonthRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .eo_month import EoMonthRequest
		return EoMonthRequest(self.request_adapter, path_parameters)

	def erf(self,
		drive_id: str,
		driveItem_id: str,
	) -> ErfRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .erf import ErfRequest
		return ErfRequest(self.request_adapter, path_parameters)

	def erf__precise(self,
		drive_id: str,
		driveItem_id: str,
	) -> Erf_PreciseRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .erf__precise import Erf_PreciseRequest
		return Erf_PreciseRequest(self.request_adapter, path_parameters)

	def erf_c(self,
		drive_id: str,
		driveItem_id: str,
	) -> ErfCRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .erf_c import ErfCRequest
		return ErfCRequest(self.request_adapter, path_parameters)

	def erf_c__precise(self,
		drive_id: str,
		driveItem_id: str,
	) -> ErfC_PreciseRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .erf_c__precise import ErfC_PreciseRequest
		return ErfC_PreciseRequest(self.request_adapter, path_parameters)

	def error__type(self,
		drive_id: str,
		driveItem_id: str,
	) -> Error_TypeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .error__type import Error_TypeRequest
		return Error_TypeRequest(self.request_adapter, path_parameters)

	def even(self,
		drive_id: str,
		driveItem_id: str,
	) -> EvenRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .even import EvenRequest
		return EvenRequest(self.request_adapter, path_parameters)

	def exact(self,
		drive_id: str,
		driveItem_id: str,
	) -> ExactRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .exact import ExactRequest
		return ExactRequest(self.request_adapter, path_parameters)

	def exp(self,
		drive_id: str,
		driveItem_id: str,
	) -> ExpRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .exp import ExpRequest
		return ExpRequest(self.request_adapter, path_parameters)

	def expon__dist(self,
		drive_id: str,
		driveItem_id: str,
	) -> Expon_DistRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .expon__dist import Expon_DistRequest
		return Expon_DistRequest(self.request_adapter, path_parameters)

	def f__dist(self,
		drive_id: str,
		driveItem_id: str,
	) -> F_DistRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .f__dist import F_DistRequest
		return F_DistRequest(self.request_adapter, path_parameters)

	def f__dist__r_t(self,
		drive_id: str,
		driveItem_id: str,
	) -> F_Dist_RTRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .f__dist__r_t import F_Dist_RTRequest
		return F_Dist_RTRequest(self.request_adapter, path_parameters)

	def f__inv(self,
		drive_id: str,
		driveItem_id: str,
	) -> F_InvRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .f__inv import F_InvRequest
		return F_InvRequest(self.request_adapter, path_parameters)

	def f__inv__r_t(self,
		drive_id: str,
		driveItem_id: str,
	) -> F_Inv_RTRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .f__inv__r_t import F_Inv_RTRequest
		return F_Inv_RTRequest(self.request_adapter, path_parameters)

	def fact(self,
		drive_id: str,
		driveItem_id: str,
	) -> FactRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .fact import FactRequest
		return FactRequest(self.request_adapter, path_parameters)

	def fact_double(self,
		drive_id: str,
		driveItem_id: str,
	) -> FactDoubleRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .fact_double import FactDoubleRequest
		return FactDoubleRequest(self.request_adapter, path_parameters)

	def false(self,
		drive_id: str,
		driveItem_id: str,
	) -> FalseRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .false import FalseRequest
		return FalseRequest(self.request_adapter, path_parameters)

	def find(self,
		drive_id: str,
		driveItem_id: str,
	) -> FindRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .find import FindRequest
		return FindRequest(self.request_adapter, path_parameters)

	def find_b(self,
		drive_id: str,
		driveItem_id: str,
	) -> FindBRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .find_b import FindBRequest
		return FindBRequest(self.request_adapter, path_parameters)

	def fisher(self,
		drive_id: str,
		driveItem_id: str,
	) -> FisherRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .fisher import FisherRequest
		return FisherRequest(self.request_adapter, path_parameters)

	def fisher_inv(self,
		drive_id: str,
		driveItem_id: str,
	) -> FisherInvRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .fisher_inv import FisherInvRequest
		return FisherInvRequest(self.request_adapter, path_parameters)

	def fixed(self,
		drive_id: str,
		driveItem_id: str,
	) -> FixedRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .fixed import FixedRequest
		return FixedRequest(self.request_adapter, path_parameters)

	def floor__math(self,
		drive_id: str,
		driveItem_id: str,
	) -> Floor_MathRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .floor__math import Floor_MathRequest
		return Floor_MathRequest(self.request_adapter, path_parameters)

	def floor__precise(self,
		drive_id: str,
		driveItem_id: str,
	) -> Floor_PreciseRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .floor__precise import Floor_PreciseRequest
		return Floor_PreciseRequest(self.request_adapter, path_parameters)

	def fv(self,
		drive_id: str,
		driveItem_id: str,
	) -> FvRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .fv import FvRequest
		return FvRequest(self.request_adapter, path_parameters)

	def fvschedule(self,
		drive_id: str,
		driveItem_id: str,
	) -> FvscheduleRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .fvschedule import FvscheduleRequest
		return FvscheduleRequest(self.request_adapter, path_parameters)

	def gamma(self,
		drive_id: str,
		driveItem_id: str,
	) -> GammaRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .gamma import GammaRequest
		return GammaRequest(self.request_adapter, path_parameters)

	def gamma__dist(self,
		drive_id: str,
		driveItem_id: str,
	) -> Gamma_DistRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .gamma__dist import Gamma_DistRequest
		return Gamma_DistRequest(self.request_adapter, path_parameters)

	def gamma__inv(self,
		drive_id: str,
		driveItem_id: str,
	) -> Gamma_InvRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .gamma__inv import Gamma_InvRequest
		return Gamma_InvRequest(self.request_adapter, path_parameters)

	def gamma_ln(self,
		drive_id: str,
		driveItem_id: str,
	) -> GammaLnRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .gamma_ln import GammaLnRequest
		return GammaLnRequest(self.request_adapter, path_parameters)

	def gamma_ln__precise(self,
		drive_id: str,
		driveItem_id: str,
	) -> GammaLn_PreciseRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .gamma_ln__precise import GammaLn_PreciseRequest
		return GammaLn_PreciseRequest(self.request_adapter, path_parameters)

	def gauss(self,
		drive_id: str,
		driveItem_id: str,
	) -> GaussRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .gauss import GaussRequest
		return GaussRequest(self.request_adapter, path_parameters)

	def gcd(self,
		drive_id: str,
		driveItem_id: str,
	) -> GcdRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .gcd import GcdRequest
		return GcdRequest(self.request_adapter, path_parameters)

	def geo_mean(self,
		drive_id: str,
		driveItem_id: str,
	) -> GeoMeanRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .geo_mean import GeoMeanRequest
		return GeoMeanRequest(self.request_adapter, path_parameters)

	def ge_step(self,
		drive_id: str,
		driveItem_id: str,
	) -> GeStepRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .ge_step import GeStepRequest
		return GeStepRequest(self.request_adapter, path_parameters)

	def har_mean(self,
		drive_id: str,
		driveItem_id: str,
	) -> HarMeanRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .har_mean import HarMeanRequest
		return HarMeanRequest(self.request_adapter, path_parameters)

	def hex2_bin(self,
		drive_id: str,
		driveItem_id: str,
	) -> Hex2BinRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .hex2_bin import Hex2BinRequest
		return Hex2BinRequest(self.request_adapter, path_parameters)

	def hex2_dec(self,
		drive_id: str,
		driveItem_id: str,
	) -> Hex2DecRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .hex2_dec import Hex2DecRequest
		return Hex2DecRequest(self.request_adapter, path_parameters)

	def hex2_oct(self,
		drive_id: str,
		driveItem_id: str,
	) -> Hex2OctRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .hex2_oct import Hex2OctRequest
		return Hex2OctRequest(self.request_adapter, path_parameters)

	def hlookup(self,
		drive_id: str,
		driveItem_id: str,
	) -> HlookupRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .hlookup import HlookupRequest
		return HlookupRequest(self.request_adapter, path_parameters)

	def hour(self,
		drive_id: str,
		driveItem_id: str,
	) -> HourRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .hour import HourRequest
		return HourRequest(self.request_adapter, path_parameters)

	def hyperlink(self,
		drive_id: str,
		driveItem_id: str,
	) -> HyperlinkRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .hyperlink import HyperlinkRequest
		return HyperlinkRequest(self.request_adapter, path_parameters)

	def hyp_geom__dist(self,
		drive_id: str,
		driveItem_id: str,
	) -> HypGeom_DistRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .hyp_geom__dist import HypGeom_DistRequest
		return HypGeom_DistRequest(self.request_adapter, path_parameters)

	def if(self,
		drive_id: str,
		driveItem_id: str,
	) -> IfRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .if import IfRequest
		return IfRequest(self.request_adapter, path_parameters)

	def im_abs(self,
		drive_id: str,
		driveItem_id: str,
	) -> ImAbsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .im_abs import ImAbsRequest
		return ImAbsRequest(self.request_adapter, path_parameters)

	def imaginary(self,
		drive_id: str,
		driveItem_id: str,
	) -> ImaginaryRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .imaginary import ImaginaryRequest
		return ImaginaryRequest(self.request_adapter, path_parameters)

	def im_argument(self,
		drive_id: str,
		driveItem_id: str,
	) -> ImArgumentRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .im_argument import ImArgumentRequest
		return ImArgumentRequest(self.request_adapter, path_parameters)

	def im_conjugate(self,
		drive_id: str,
		driveItem_id: str,
	) -> ImConjugateRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .im_conjugate import ImConjugateRequest
		return ImConjugateRequest(self.request_adapter, path_parameters)

	def im_cos(self,
		drive_id: str,
		driveItem_id: str,
	) -> ImCosRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .im_cos import ImCosRequest
		return ImCosRequest(self.request_adapter, path_parameters)

	def im_cosh(self,
		drive_id: str,
		driveItem_id: str,
	) -> ImCoshRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .im_cosh import ImCoshRequest
		return ImCoshRequest(self.request_adapter, path_parameters)

	def im_cot(self,
		drive_id: str,
		driveItem_id: str,
	) -> ImCotRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .im_cot import ImCotRequest
		return ImCotRequest(self.request_adapter, path_parameters)

	def im_csc(self,
		drive_id: str,
		driveItem_id: str,
	) -> ImCscRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .im_csc import ImCscRequest
		return ImCscRequest(self.request_adapter, path_parameters)

	def im_csch(self,
		drive_id: str,
		driveItem_id: str,
	) -> ImCschRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .im_csch import ImCschRequest
		return ImCschRequest(self.request_adapter, path_parameters)

	def im_div(self,
		drive_id: str,
		driveItem_id: str,
	) -> ImDivRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .im_div import ImDivRequest
		return ImDivRequest(self.request_adapter, path_parameters)

	def im_exp(self,
		drive_id: str,
		driveItem_id: str,
	) -> ImExpRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .im_exp import ImExpRequest
		return ImExpRequest(self.request_adapter, path_parameters)

	def im_ln(self,
		drive_id: str,
		driveItem_id: str,
	) -> ImLnRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .im_ln import ImLnRequest
		return ImLnRequest(self.request_adapter, path_parameters)

	def im_log10(self,
		drive_id: str,
		driveItem_id: str,
	) -> ImLog10Request:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .im_log10 import ImLog10Request
		return ImLog10Request(self.request_adapter, path_parameters)

	def im_log2(self,
		drive_id: str,
		driveItem_id: str,
	) -> ImLog2Request:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .im_log2 import ImLog2Request
		return ImLog2Request(self.request_adapter, path_parameters)

	def im_power(self,
		drive_id: str,
		driveItem_id: str,
	) -> ImPowerRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .im_power import ImPowerRequest
		return ImPowerRequest(self.request_adapter, path_parameters)

	def im_product(self,
		drive_id: str,
		driveItem_id: str,
	) -> ImProductRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .im_product import ImProductRequest
		return ImProductRequest(self.request_adapter, path_parameters)

	def im_real(self,
		drive_id: str,
		driveItem_id: str,
	) -> ImRealRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .im_real import ImRealRequest
		return ImRealRequest(self.request_adapter, path_parameters)

	def im_sec(self,
		drive_id: str,
		driveItem_id: str,
	) -> ImSecRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .im_sec import ImSecRequest
		return ImSecRequest(self.request_adapter, path_parameters)

	def im_sech(self,
		drive_id: str,
		driveItem_id: str,
	) -> ImSechRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .im_sech import ImSechRequest
		return ImSechRequest(self.request_adapter, path_parameters)

	def im_sin(self,
		drive_id: str,
		driveItem_id: str,
	) -> ImSinRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .im_sin import ImSinRequest
		return ImSinRequest(self.request_adapter, path_parameters)

	def im_sinh(self,
		drive_id: str,
		driveItem_id: str,
	) -> ImSinhRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .im_sinh import ImSinhRequest
		return ImSinhRequest(self.request_adapter, path_parameters)

	def im_sqrt(self,
		drive_id: str,
		driveItem_id: str,
	) -> ImSqrtRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .im_sqrt import ImSqrtRequest
		return ImSqrtRequest(self.request_adapter, path_parameters)

	def im_sub(self,
		drive_id: str,
		driveItem_id: str,
	) -> ImSubRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .im_sub import ImSubRequest
		return ImSubRequest(self.request_adapter, path_parameters)

	def im_sum(self,
		drive_id: str,
		driveItem_id: str,
	) -> ImSumRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .im_sum import ImSumRequest
		return ImSumRequest(self.request_adapter, path_parameters)

	def im_tan(self,
		drive_id: str,
		driveItem_id: str,
	) -> ImTanRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .im_tan import ImTanRequest
		return ImTanRequest(self.request_adapter, path_parameters)

	def int(self,
		drive_id: str,
		driveItem_id: str,
	) -> IntRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .int import IntRequest
		return IntRequest(self.request_adapter, path_parameters)

	def int_rate(self,
		drive_id: str,
		driveItem_id: str,
	) -> IntRateRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .int_rate import IntRateRequest
		return IntRateRequest(self.request_adapter, path_parameters)

	def ipmt(self,
		drive_id: str,
		driveItem_id: str,
	) -> IpmtRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .ipmt import IpmtRequest
		return IpmtRequest(self.request_adapter, path_parameters)

	def irr(self,
		drive_id: str,
		driveItem_id: str,
	) -> IrrRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .irr import IrrRequest
		return IrrRequest(self.request_adapter, path_parameters)

	def is_err(self,
		drive_id: str,
		driveItem_id: str,
	) -> IsErrRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .is_err import IsErrRequest
		return IsErrRequest(self.request_adapter, path_parameters)

	def is_error(self,
		drive_id: str,
		driveItem_id: str,
	) -> IsErrorRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .is_error import IsErrorRequest
		return IsErrorRequest(self.request_adapter, path_parameters)

	def is_even(self,
		drive_id: str,
		driveItem_id: str,
	) -> IsEvenRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .is_even import IsEvenRequest
		return IsEvenRequest(self.request_adapter, path_parameters)

	def is_formula(self,
		drive_id: str,
		driveItem_id: str,
	) -> IsFormulaRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .is_formula import IsFormulaRequest
		return IsFormulaRequest(self.request_adapter, path_parameters)

	def is_logical(self,
		drive_id: str,
		driveItem_id: str,
	) -> IsLogicalRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .is_logical import IsLogicalRequest
		return IsLogicalRequest(self.request_adapter, path_parameters)

	def is_n_a(self,
		drive_id: str,
		driveItem_id: str,
	) -> IsNARequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .is_n_a import IsNARequest
		return IsNARequest(self.request_adapter, path_parameters)

	def is_non_text(self,
		drive_id: str,
		driveItem_id: str,
	) -> IsNonTextRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .is_non_text import IsNonTextRequest
		return IsNonTextRequest(self.request_adapter, path_parameters)

	def is_number(self,
		drive_id: str,
		driveItem_id: str,
	) -> IsNumberRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .is_number import IsNumberRequest
		return IsNumberRequest(self.request_adapter, path_parameters)

	def iso__ceiling(self,
		drive_id: str,
		driveItem_id: str,
	) -> Iso_CeilingRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .iso__ceiling import Iso_CeilingRequest
		return Iso_CeilingRequest(self.request_adapter, path_parameters)

	def is_odd(self,
		drive_id: str,
		driveItem_id: str,
	) -> IsOddRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .is_odd import IsOddRequest
		return IsOddRequest(self.request_adapter, path_parameters)

	def iso_week_num(self,
		drive_id: str,
		driveItem_id: str,
	) -> IsoWeekNumRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .iso_week_num import IsoWeekNumRequest
		return IsoWeekNumRequest(self.request_adapter, path_parameters)

	def ispmt(self,
		drive_id: str,
		driveItem_id: str,
	) -> IspmtRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .ispmt import IspmtRequest
		return IspmtRequest(self.request_adapter, path_parameters)

	def isref(self,
		drive_id: str,
		driveItem_id: str,
	) -> IsrefRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .isref import IsrefRequest
		return IsrefRequest(self.request_adapter, path_parameters)

	def is_text(self,
		drive_id: str,
		driveItem_id: str,
	) -> IsTextRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .is_text import IsTextRequest
		return IsTextRequest(self.request_adapter, path_parameters)

	def kurt(self,
		drive_id: str,
		driveItem_id: str,
	) -> KurtRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .kurt import KurtRequest
		return KurtRequest(self.request_adapter, path_parameters)

	def large(self,
		drive_id: str,
		driveItem_id: str,
	) -> LargeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .large import LargeRequest
		return LargeRequest(self.request_adapter, path_parameters)

	def lcm(self,
		drive_id: str,
		driveItem_id: str,
	) -> LcmRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .lcm import LcmRequest
		return LcmRequest(self.request_adapter, path_parameters)

	def left(self,
		drive_id: str,
		driveItem_id: str,
	) -> LeftRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .left import LeftRequest
		return LeftRequest(self.request_adapter, path_parameters)

	def leftb(self,
		drive_id: str,
		driveItem_id: str,
	) -> LeftbRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .leftb import LeftbRequest
		return LeftbRequest(self.request_adapter, path_parameters)

	def len(self,
		drive_id: str,
		driveItem_id: str,
	) -> LenRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .len import LenRequest
		return LenRequest(self.request_adapter, path_parameters)

	def lenb(self,
		drive_id: str,
		driveItem_id: str,
	) -> LenbRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .lenb import LenbRequest
		return LenbRequest(self.request_adapter, path_parameters)

	def ln(self,
		drive_id: str,
		driveItem_id: str,
	) -> LnRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .ln import LnRequest
		return LnRequest(self.request_adapter, path_parameters)

	def log(self,
		drive_id: str,
		driveItem_id: str,
	) -> LogRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .log import LogRequest
		return LogRequest(self.request_adapter, path_parameters)

	def log10(self,
		drive_id: str,
		driveItem_id: str,
	) -> Log10Request:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .log10 import Log10Request
		return Log10Request(self.request_adapter, path_parameters)

	def log_norm__dist(self,
		drive_id: str,
		driveItem_id: str,
	) -> LogNorm_DistRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .log_norm__dist import LogNorm_DistRequest
		return LogNorm_DistRequest(self.request_adapter, path_parameters)

	def log_norm__inv(self,
		drive_id: str,
		driveItem_id: str,
	) -> LogNorm_InvRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .log_norm__inv import LogNorm_InvRequest
		return LogNorm_InvRequest(self.request_adapter, path_parameters)

	def lookup(self,
		drive_id: str,
		driveItem_id: str,
	) -> LookupRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .lookup import LookupRequest
		return LookupRequest(self.request_adapter, path_parameters)

	def lower(self,
		drive_id: str,
		driveItem_id: str,
	) -> LowerRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .lower import LowerRequest
		return LowerRequest(self.request_adapter, path_parameters)

	def match(self,
		drive_id: str,
		driveItem_id: str,
	) -> MatchRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .match import MatchRequest
		return MatchRequest(self.request_adapter, path_parameters)

	def max(self,
		drive_id: str,
		driveItem_id: str,
	) -> MaxRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .max import MaxRequest
		return MaxRequest(self.request_adapter, path_parameters)

	def max_a(self,
		drive_id: str,
		driveItem_id: str,
	) -> MaxARequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .max_a import MaxARequest
		return MaxARequest(self.request_adapter, path_parameters)

	def mduration(self,
		drive_id: str,
		driveItem_id: str,
	) -> MdurationRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .mduration import MdurationRequest
		return MdurationRequest(self.request_adapter, path_parameters)

	def median(self,
		drive_id: str,
		driveItem_id: str,
	) -> MedianRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .median import MedianRequest
		return MedianRequest(self.request_adapter, path_parameters)

	def mid(self,
		drive_id: str,
		driveItem_id: str,
	) -> MidRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .mid import MidRequest
		return MidRequest(self.request_adapter, path_parameters)

	def midb(self,
		drive_id: str,
		driveItem_id: str,
	) -> MidbRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .midb import MidbRequest
		return MidbRequest(self.request_adapter, path_parameters)

	def min(self,
		drive_id: str,
		driveItem_id: str,
	) -> MinRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .min import MinRequest
		return MinRequest(self.request_adapter, path_parameters)

	def min_a(self,
		drive_id: str,
		driveItem_id: str,
	) -> MinARequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .min_a import MinARequest
		return MinARequest(self.request_adapter, path_parameters)

	def minute(self,
		drive_id: str,
		driveItem_id: str,
	) -> MinuteRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .minute import MinuteRequest
		return MinuteRequest(self.request_adapter, path_parameters)

	def mirr(self,
		drive_id: str,
		driveItem_id: str,
	) -> MirrRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .mirr import MirrRequest
		return MirrRequest(self.request_adapter, path_parameters)

	def mod(self,
		drive_id: str,
		driveItem_id: str,
	) -> ModRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .mod import ModRequest
		return ModRequest(self.request_adapter, path_parameters)

	def month(self,
		drive_id: str,
		driveItem_id: str,
	) -> MonthRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .month import MonthRequest
		return MonthRequest(self.request_adapter, path_parameters)

	def mround(self,
		drive_id: str,
		driveItem_id: str,
	) -> MroundRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .mround import MroundRequest
		return MroundRequest(self.request_adapter, path_parameters)

	def multi_nomial(self,
		drive_id: str,
		driveItem_id: str,
	) -> MultiNomialRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .multi_nomial import MultiNomialRequest
		return MultiNomialRequest(self.request_adapter, path_parameters)

	def n(self,
		drive_id: str,
		driveItem_id: str,
	) -> NRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .n import NRequest
		return NRequest(self.request_adapter, path_parameters)

	def na(self,
		drive_id: str,
		driveItem_id: str,
	) -> NaRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .na import NaRequest
		return NaRequest(self.request_adapter, path_parameters)

	def neg_binom__dist(self,
		drive_id: str,
		driveItem_id: str,
	) -> NegBinom_DistRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .neg_binom__dist import NegBinom_DistRequest
		return NegBinom_DistRequest(self.request_adapter, path_parameters)

	def network_days(self,
		drive_id: str,
		driveItem_id: str,
	) -> NetworkDaysRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .network_days import NetworkDaysRequest
		return NetworkDaysRequest(self.request_adapter, path_parameters)

	def network_days__intl(self,
		drive_id: str,
		driveItem_id: str,
	) -> NetworkDays_IntlRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .network_days__intl import NetworkDays_IntlRequest
		return NetworkDays_IntlRequest(self.request_adapter, path_parameters)

	def nominal(self,
		drive_id: str,
		driveItem_id: str,
	) -> NominalRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .nominal import NominalRequest
		return NominalRequest(self.request_adapter, path_parameters)

	def norm__dist(self,
		drive_id: str,
		driveItem_id: str,
	) -> Norm_DistRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .norm__dist import Norm_DistRequest
		return Norm_DistRequest(self.request_adapter, path_parameters)

	def norm__inv(self,
		drive_id: str,
		driveItem_id: str,
	) -> Norm_InvRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .norm__inv import Norm_InvRequest
		return Norm_InvRequest(self.request_adapter, path_parameters)

	def norm__s__dist(self,
		drive_id: str,
		driveItem_id: str,
	) -> Norm_S_DistRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .norm__s__dist import Norm_S_DistRequest
		return Norm_S_DistRequest(self.request_adapter, path_parameters)

	def norm__s__inv(self,
		drive_id: str,
		driveItem_id: str,
	) -> Norm_S_InvRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .norm__s__inv import Norm_S_InvRequest
		return Norm_S_InvRequest(self.request_adapter, path_parameters)

	def not(self,
		drive_id: str,
		driveItem_id: str,
	) -> NotRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .not import NotRequest
		return NotRequest(self.request_adapter, path_parameters)

	def now(self,
		drive_id: str,
		driveItem_id: str,
	) -> NowRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .now import NowRequest
		return NowRequest(self.request_adapter, path_parameters)

	def nper(self,
		drive_id: str,
		driveItem_id: str,
	) -> NperRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .nper import NperRequest
		return NperRequest(self.request_adapter, path_parameters)

	def npv(self,
		drive_id: str,
		driveItem_id: str,
	) -> NpvRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .npv import NpvRequest
		return NpvRequest(self.request_adapter, path_parameters)

	def number_value(self,
		drive_id: str,
		driveItem_id: str,
	) -> NumberValueRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .number_value import NumberValueRequest
		return NumberValueRequest(self.request_adapter, path_parameters)

	def oct2_bin(self,
		drive_id: str,
		driveItem_id: str,
	) -> Oct2BinRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .oct2_bin import Oct2BinRequest
		return Oct2BinRequest(self.request_adapter, path_parameters)

	def oct2_dec(self,
		drive_id: str,
		driveItem_id: str,
	) -> Oct2DecRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .oct2_dec import Oct2DecRequest
		return Oct2DecRequest(self.request_adapter, path_parameters)

	def oct2_hex(self,
		drive_id: str,
		driveItem_id: str,
	) -> Oct2HexRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .oct2_hex import Oct2HexRequest
		return Oct2HexRequest(self.request_adapter, path_parameters)

	def odd(self,
		drive_id: str,
		driveItem_id: str,
	) -> OddRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .odd import OddRequest
		return OddRequest(self.request_adapter, path_parameters)

	def odd_f_price(self,
		drive_id: str,
		driveItem_id: str,
	) -> OddFPriceRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .odd_f_price import OddFPriceRequest
		return OddFPriceRequest(self.request_adapter, path_parameters)

	def odd_f_yield(self,
		drive_id: str,
		driveItem_id: str,
	) -> OddFYieldRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .odd_f_yield import OddFYieldRequest
		return OddFYieldRequest(self.request_adapter, path_parameters)

	def odd_l_price(self,
		drive_id: str,
		driveItem_id: str,
	) -> OddLPriceRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .odd_l_price import OddLPriceRequest
		return OddLPriceRequest(self.request_adapter, path_parameters)

	def odd_l_yield(self,
		drive_id: str,
		driveItem_id: str,
	) -> OddLYieldRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .odd_l_yield import OddLYieldRequest
		return OddLYieldRequest(self.request_adapter, path_parameters)

	def or(self,
		drive_id: str,
		driveItem_id: str,
	) -> OrRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .or import OrRequest
		return OrRequest(self.request_adapter, path_parameters)

	def pduration(self,
		drive_id: str,
		driveItem_id: str,
	) -> PdurationRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .pduration import PdurationRequest
		return PdurationRequest(self.request_adapter, path_parameters)

	def percentile__exc(self,
		drive_id: str,
		driveItem_id: str,
	) -> Percentile_ExcRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .percentile__exc import Percentile_ExcRequest
		return Percentile_ExcRequest(self.request_adapter, path_parameters)

	def percentile__inc(self,
		drive_id: str,
		driveItem_id: str,
	) -> Percentile_IncRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .percentile__inc import Percentile_IncRequest
		return Percentile_IncRequest(self.request_adapter, path_parameters)

	def percent_rank__exc(self,
		drive_id: str,
		driveItem_id: str,
	) -> PercentRank_ExcRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .percent_rank__exc import PercentRank_ExcRequest
		return PercentRank_ExcRequest(self.request_adapter, path_parameters)

	def percent_rank__inc(self,
		drive_id: str,
		driveItem_id: str,
	) -> PercentRank_IncRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .percent_rank__inc import PercentRank_IncRequest
		return PercentRank_IncRequest(self.request_adapter, path_parameters)

	def permut(self,
		drive_id: str,
		driveItem_id: str,
	) -> PermutRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .permut import PermutRequest
		return PermutRequest(self.request_adapter, path_parameters)

	def permutationa(self,
		drive_id: str,
		driveItem_id: str,
	) -> PermutationaRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .permutationa import PermutationaRequest
		return PermutationaRequest(self.request_adapter, path_parameters)

	def phi(self,
		drive_id: str,
		driveItem_id: str,
	) -> PhiRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .phi import PhiRequest
		return PhiRequest(self.request_adapter, path_parameters)

	def pi(self,
		drive_id: str,
		driveItem_id: str,
	) -> PiRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .pi import PiRequest
		return PiRequest(self.request_adapter, path_parameters)

	def pmt(self,
		drive_id: str,
		driveItem_id: str,
	) -> PmtRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .pmt import PmtRequest
		return PmtRequest(self.request_adapter, path_parameters)

	def poisson__dist(self,
		drive_id: str,
		driveItem_id: str,
	) -> Poisson_DistRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .poisson__dist import Poisson_DistRequest
		return Poisson_DistRequest(self.request_adapter, path_parameters)

	def power(self,
		drive_id: str,
		driveItem_id: str,
	) -> PowerRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .power import PowerRequest
		return PowerRequest(self.request_adapter, path_parameters)

	def ppmt(self,
		drive_id: str,
		driveItem_id: str,
	) -> PpmtRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .ppmt import PpmtRequest
		return PpmtRequest(self.request_adapter, path_parameters)

	def price(self,
		drive_id: str,
		driveItem_id: str,
	) -> PriceRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .price import PriceRequest
		return PriceRequest(self.request_adapter, path_parameters)

	def price_disc(self,
		drive_id: str,
		driveItem_id: str,
	) -> PriceDiscRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .price_disc import PriceDiscRequest
		return PriceDiscRequest(self.request_adapter, path_parameters)

	def price_mat(self,
		drive_id: str,
		driveItem_id: str,
	) -> PriceMatRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .price_mat import PriceMatRequest
		return PriceMatRequest(self.request_adapter, path_parameters)

	def product(self,
		drive_id: str,
		driveItem_id: str,
	) -> ProductRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .product import ProductRequest
		return ProductRequest(self.request_adapter, path_parameters)

	def proper(self,
		drive_id: str,
		driveItem_id: str,
	) -> ProperRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .proper import ProperRequest
		return ProperRequest(self.request_adapter, path_parameters)

	def pv(self,
		drive_id: str,
		driveItem_id: str,
	) -> PvRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .pv import PvRequest
		return PvRequest(self.request_adapter, path_parameters)

	def quartile__exc(self,
		drive_id: str,
		driveItem_id: str,
	) -> Quartile_ExcRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .quartile__exc import Quartile_ExcRequest
		return Quartile_ExcRequest(self.request_adapter, path_parameters)

	def quartile__inc(self,
		drive_id: str,
		driveItem_id: str,
	) -> Quartile_IncRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .quartile__inc import Quartile_IncRequest
		return Quartile_IncRequest(self.request_adapter, path_parameters)

	def quotient(self,
		drive_id: str,
		driveItem_id: str,
	) -> QuotientRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .quotient import QuotientRequest
		return QuotientRequest(self.request_adapter, path_parameters)

	def radians(self,
		drive_id: str,
		driveItem_id: str,
	) -> RadiansRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .radians import RadiansRequest
		return RadiansRequest(self.request_adapter, path_parameters)

	def rand(self,
		drive_id: str,
		driveItem_id: str,
	) -> RandRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .rand import RandRequest
		return RandRequest(self.request_adapter, path_parameters)

	def rand_between(self,
		drive_id: str,
		driveItem_id: str,
	) -> RandBetweenRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .rand_between import RandBetweenRequest
		return RandBetweenRequest(self.request_adapter, path_parameters)

	def rank__avg(self,
		drive_id: str,
		driveItem_id: str,
	) -> Rank_AvgRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .rank__avg import Rank_AvgRequest
		return Rank_AvgRequest(self.request_adapter, path_parameters)

	def rank__eq(self,
		drive_id: str,
		driveItem_id: str,
	) -> Rank_EqRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .rank__eq import Rank_EqRequest
		return Rank_EqRequest(self.request_adapter, path_parameters)

	def rate(self,
		drive_id: str,
		driveItem_id: str,
	) -> RateRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .rate import RateRequest
		return RateRequest(self.request_adapter, path_parameters)

	def received(self,
		drive_id: str,
		driveItem_id: str,
	) -> ReceivedRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .received import ReceivedRequest
		return ReceivedRequest(self.request_adapter, path_parameters)

	def replace(self,
		drive_id: str,
		driveItem_id: str,
	) -> ReplaceRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .replace import ReplaceRequest
		return ReplaceRequest(self.request_adapter, path_parameters)

	def replace_b(self,
		drive_id: str,
		driveItem_id: str,
	) -> ReplaceBRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .replace_b import ReplaceBRequest
		return ReplaceBRequest(self.request_adapter, path_parameters)

	def rept(self,
		drive_id: str,
		driveItem_id: str,
	) -> ReptRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .rept import ReptRequest
		return ReptRequest(self.request_adapter, path_parameters)

	def right(self,
		drive_id: str,
		driveItem_id: str,
	) -> RightRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .right import RightRequest
		return RightRequest(self.request_adapter, path_parameters)

	def rightb(self,
		drive_id: str,
		driveItem_id: str,
	) -> RightbRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .rightb import RightbRequest
		return RightbRequest(self.request_adapter, path_parameters)

	def roman(self,
		drive_id: str,
		driveItem_id: str,
	) -> RomanRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .roman import RomanRequest
		return RomanRequest(self.request_adapter, path_parameters)

	def round(self,
		drive_id: str,
		driveItem_id: str,
	) -> RoundRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .round import RoundRequest
		return RoundRequest(self.request_adapter, path_parameters)

	def round_down(self,
		drive_id: str,
		driveItem_id: str,
	) -> RoundDownRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .round_down import RoundDownRequest
		return RoundDownRequest(self.request_adapter, path_parameters)

	def round_up(self,
		drive_id: str,
		driveItem_id: str,
	) -> RoundUpRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .round_up import RoundUpRequest
		return RoundUpRequest(self.request_adapter, path_parameters)

	def rows(self,
		drive_id: str,
		driveItem_id: str,
	) -> RowsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .rows import RowsRequest
		return RowsRequest(self.request_adapter, path_parameters)

	def rri(self,
		drive_id: str,
		driveItem_id: str,
	) -> RriRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .rri import RriRequest
		return RriRequest(self.request_adapter, path_parameters)

	def sec(self,
		drive_id: str,
		driveItem_id: str,
	) -> SecRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .sec import SecRequest
		return SecRequest(self.request_adapter, path_parameters)

	def sech(self,
		drive_id: str,
		driveItem_id: str,
	) -> SechRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .sech import SechRequest
		return SechRequest(self.request_adapter, path_parameters)

	def second(self,
		drive_id: str,
		driveItem_id: str,
	) -> SecondRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .second import SecondRequest
		return SecondRequest(self.request_adapter, path_parameters)

	def series_sum(self,
		drive_id: str,
		driveItem_id: str,
	) -> SeriesSumRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .series_sum import SeriesSumRequest
		return SeriesSumRequest(self.request_adapter, path_parameters)

	def sheet(self,
		drive_id: str,
		driveItem_id: str,
	) -> SheetRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .sheet import SheetRequest
		return SheetRequest(self.request_adapter, path_parameters)

	def sheets(self,
		drive_id: str,
		driveItem_id: str,
	) -> SheetsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .sheets import SheetsRequest
		return SheetsRequest(self.request_adapter, path_parameters)

	def sign(self,
		drive_id: str,
		driveItem_id: str,
	) -> SignRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .sign import SignRequest
		return SignRequest(self.request_adapter, path_parameters)

	def sin(self,
		drive_id: str,
		driveItem_id: str,
	) -> SinRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .sin import SinRequest
		return SinRequest(self.request_adapter, path_parameters)

	def sinh(self,
		drive_id: str,
		driveItem_id: str,
	) -> SinhRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .sinh import SinhRequest
		return SinhRequest(self.request_adapter, path_parameters)

	def skew(self,
		drive_id: str,
		driveItem_id: str,
	) -> SkewRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .skew import SkewRequest
		return SkewRequest(self.request_adapter, path_parameters)

	def skew_p(self,
		drive_id: str,
		driveItem_id: str,
	) -> Skew_pRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .skew_p import Skew_pRequest
		return Skew_pRequest(self.request_adapter, path_parameters)

	def sln(self,
		drive_id: str,
		driveItem_id: str,
	) -> SlnRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .sln import SlnRequest
		return SlnRequest(self.request_adapter, path_parameters)

	def small(self,
		drive_id: str,
		driveItem_id: str,
	) -> SmallRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .small import SmallRequest
		return SmallRequest(self.request_adapter, path_parameters)

	def sqrt(self,
		drive_id: str,
		driveItem_id: str,
	) -> SqrtRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .sqrt import SqrtRequest
		return SqrtRequest(self.request_adapter, path_parameters)

	def sqrt_pi(self,
		drive_id: str,
		driveItem_id: str,
	) -> SqrtPiRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .sqrt_pi import SqrtPiRequest
		return SqrtPiRequest(self.request_adapter, path_parameters)

	def standardize(self,
		drive_id: str,
		driveItem_id: str,
	) -> StandardizeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .standardize import StandardizeRequest
		return StandardizeRequest(self.request_adapter, path_parameters)

	def st_dev__p(self,
		drive_id: str,
		driveItem_id: str,
	) -> StDev_PRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .st_dev__p import StDev_PRequest
		return StDev_PRequest(self.request_adapter, path_parameters)

	def st_dev__s(self,
		drive_id: str,
		driveItem_id: str,
	) -> StDev_SRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .st_dev__s import StDev_SRequest
		return StDev_SRequest(self.request_adapter, path_parameters)

	def st_dev_a(self,
		drive_id: str,
		driveItem_id: str,
	) -> StDevARequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .st_dev_a import StDevARequest
		return StDevARequest(self.request_adapter, path_parameters)

	def st_dev_p_a(self,
		drive_id: str,
		driveItem_id: str,
	) -> StDevPARequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .st_dev_p_a import StDevPARequest
		return StDevPARequest(self.request_adapter, path_parameters)

	def substitute(self,
		drive_id: str,
		driveItem_id: str,
	) -> SubstituteRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .substitute import SubstituteRequest
		return SubstituteRequest(self.request_adapter, path_parameters)

	def subtotal(self,
		drive_id: str,
		driveItem_id: str,
	) -> SubtotalRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .subtotal import SubtotalRequest
		return SubtotalRequest(self.request_adapter, path_parameters)

	def sum(self,
		drive_id: str,
		driveItem_id: str,
	) -> SumRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .sum import SumRequest
		return SumRequest(self.request_adapter, path_parameters)

	def sum_if(self,
		drive_id: str,
		driveItem_id: str,
	) -> SumIfRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .sum_if import SumIfRequest
		return SumIfRequest(self.request_adapter, path_parameters)

	def sum_ifs(self,
		drive_id: str,
		driveItem_id: str,
	) -> SumIfsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .sum_ifs import SumIfsRequest
		return SumIfsRequest(self.request_adapter, path_parameters)

	def sum_sq(self,
		drive_id: str,
		driveItem_id: str,
	) -> SumSqRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .sum_sq import SumSqRequest
		return SumSqRequest(self.request_adapter, path_parameters)

	def syd(self,
		drive_id: str,
		driveItem_id: str,
	) -> SydRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .syd import SydRequest
		return SydRequest(self.request_adapter, path_parameters)

	def t(self,
		drive_id: str,
		driveItem_id: str,
	) -> TRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .t import TRequest
		return TRequest(self.request_adapter, path_parameters)

	def t__dist(self,
		drive_id: str,
		driveItem_id: str,
	) -> T_DistRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .t__dist import T_DistRequest
		return T_DistRequest(self.request_adapter, path_parameters)

	def t__dist_2_t(self,
		drive_id: str,
		driveItem_id: str,
	) -> T_Dist_2TRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .t__dist_2_t import T_Dist_2TRequest
		return T_Dist_2TRequest(self.request_adapter, path_parameters)

	def t__dist__r_t(self,
		drive_id: str,
		driveItem_id: str,
	) -> T_Dist_RTRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .t__dist__r_t import T_Dist_RTRequest
		return T_Dist_RTRequest(self.request_adapter, path_parameters)

	def t__inv(self,
		drive_id: str,
		driveItem_id: str,
	) -> T_InvRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .t__inv import T_InvRequest
		return T_InvRequest(self.request_adapter, path_parameters)

	def t__inv_2_t(self,
		drive_id: str,
		driveItem_id: str,
	) -> T_Inv_2TRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .t__inv_2_t import T_Inv_2TRequest
		return T_Inv_2TRequest(self.request_adapter, path_parameters)

	def tan(self,
		drive_id: str,
		driveItem_id: str,
	) -> TanRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .tan import TanRequest
		return TanRequest(self.request_adapter, path_parameters)

	def tanh(self,
		drive_id: str,
		driveItem_id: str,
	) -> TanhRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .tanh import TanhRequest
		return TanhRequest(self.request_adapter, path_parameters)

	def tbill_eq(self,
		drive_id: str,
		driveItem_id: str,
	) -> TbillEqRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .tbill_eq import TbillEqRequest
		return TbillEqRequest(self.request_adapter, path_parameters)

	def tbill_price(self,
		drive_id: str,
		driveItem_id: str,
	) -> TbillPriceRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .tbill_price import TbillPriceRequest
		return TbillPriceRequest(self.request_adapter, path_parameters)

	def tbill_yield(self,
		drive_id: str,
		driveItem_id: str,
	) -> TbillYieldRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .tbill_yield import TbillYieldRequest
		return TbillYieldRequest(self.request_adapter, path_parameters)

	def text(self,
		drive_id: str,
		driveItem_id: str,
	) -> TextRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .text import TextRequest
		return TextRequest(self.request_adapter, path_parameters)

	def time(self,
		drive_id: str,
		driveItem_id: str,
	) -> TimeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .time import TimeRequest
		return TimeRequest(self.request_adapter, path_parameters)

	def timevalue(self,
		drive_id: str,
		driveItem_id: str,
	) -> TimevalueRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .timevalue import TimevalueRequest
		return TimevalueRequest(self.request_adapter, path_parameters)

	def today(self,
		drive_id: str,
		driveItem_id: str,
	) -> TodayRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .today import TodayRequest
		return TodayRequest(self.request_adapter, path_parameters)

	def trim(self,
		drive_id: str,
		driveItem_id: str,
	) -> TrimRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .trim import TrimRequest
		return TrimRequest(self.request_adapter, path_parameters)

	def trim_mean(self,
		drive_id: str,
		driveItem_id: str,
	) -> TrimMeanRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .trim_mean import TrimMeanRequest
		return TrimMeanRequest(self.request_adapter, path_parameters)

	def true(self,
		drive_id: str,
		driveItem_id: str,
	) -> TrueRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .true import TrueRequest
		return TrueRequest(self.request_adapter, path_parameters)

	def trunc(self,
		drive_id: str,
		driveItem_id: str,
	) -> TruncRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .trunc import TruncRequest
		return TruncRequest(self.request_adapter, path_parameters)

	def type(self,
		drive_id: str,
		driveItem_id: str,
	) -> TypeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .type import TypeRequest
		return TypeRequest(self.request_adapter, path_parameters)

	def unichar(self,
		drive_id: str,
		driveItem_id: str,
	) -> UnicharRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .unichar import UnicharRequest
		return UnicharRequest(self.request_adapter, path_parameters)

	def unicode(self,
		drive_id: str,
		driveItem_id: str,
	) -> UnicodeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .unicode import UnicodeRequest
		return UnicodeRequest(self.request_adapter, path_parameters)

	def upper(self,
		drive_id: str,
		driveItem_id: str,
	) -> UpperRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .upper import UpperRequest
		return UpperRequest(self.request_adapter, path_parameters)

	def usdollar(self,
		drive_id: str,
		driveItem_id: str,
	) -> UsdollarRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .usdollar import UsdollarRequest
		return UsdollarRequest(self.request_adapter, path_parameters)

	def value(self,
		drive_id: str,
		driveItem_id: str,
	) -> ValueRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .value import ValueRequest
		return ValueRequest(self.request_adapter, path_parameters)

	def var__p(self,
		drive_id: str,
		driveItem_id: str,
	) -> Var_PRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .var__p import Var_PRequest
		return Var_PRequest(self.request_adapter, path_parameters)

	def var__s(self,
		drive_id: str,
		driveItem_id: str,
	) -> Var_SRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .var__s import Var_SRequest
		return Var_SRequest(self.request_adapter, path_parameters)

	def var_a(self,
		drive_id: str,
		driveItem_id: str,
	) -> VarARequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .var_a import VarARequest
		return VarARequest(self.request_adapter, path_parameters)

	def var_p_a(self,
		drive_id: str,
		driveItem_id: str,
	) -> VarPARequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .var_p_a import VarPARequest
		return VarPARequest(self.request_adapter, path_parameters)

	def vdb(self,
		drive_id: str,
		driveItem_id: str,
	) -> VdbRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .vdb import VdbRequest
		return VdbRequest(self.request_adapter, path_parameters)

	def vlookup(self,
		drive_id: str,
		driveItem_id: str,
	) -> VlookupRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .vlookup import VlookupRequest
		return VlookupRequest(self.request_adapter, path_parameters)

	def weekday(self,
		drive_id: str,
		driveItem_id: str,
	) -> WeekdayRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .weekday import WeekdayRequest
		return WeekdayRequest(self.request_adapter, path_parameters)

	def week_num(self,
		drive_id: str,
		driveItem_id: str,
	) -> WeekNumRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .week_num import WeekNumRequest
		return WeekNumRequest(self.request_adapter, path_parameters)

	def weibull__dist(self,
		drive_id: str,
		driveItem_id: str,
	) -> Weibull_DistRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .weibull__dist import Weibull_DistRequest
		return Weibull_DistRequest(self.request_adapter, path_parameters)

	def work_day(self,
		drive_id: str,
		driveItem_id: str,
	) -> WorkDayRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .work_day import WorkDayRequest
		return WorkDayRequest(self.request_adapter, path_parameters)

	def work_day__intl(self,
		drive_id: str,
		driveItem_id: str,
	) -> WorkDay_IntlRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .work_day__intl import WorkDay_IntlRequest
		return WorkDay_IntlRequest(self.request_adapter, path_parameters)

	def xirr(self,
		drive_id: str,
		driveItem_id: str,
	) -> XirrRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .xirr import XirrRequest
		return XirrRequest(self.request_adapter, path_parameters)

	def xnpv(self,
		drive_id: str,
		driveItem_id: str,
	) -> XnpvRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .xnpv import XnpvRequest
		return XnpvRequest(self.request_adapter, path_parameters)

	def xor(self,
		drive_id: str,
		driveItem_id: str,
	) -> XorRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .xor import XorRequest
		return XorRequest(self.request_adapter, path_parameters)

	def year(self,
		drive_id: str,
		driveItem_id: str,
	) -> YearRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .year import YearRequest
		return YearRequest(self.request_adapter, path_parameters)

	def year_frac(self,
		drive_id: str,
		driveItem_id: str,
	) -> YearFracRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .year_frac import YearFracRequest
		return YearFracRequest(self.request_adapter, path_parameters)

	def yield(self,
		drive_id: str,
		driveItem_id: str,
	) -> YieldRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .yield import YieldRequest
		return YieldRequest(self.request_adapter, path_parameters)

	def yield_disc(self,
		drive_id: str,
		driveItem_id: str,
	) -> YieldDiscRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .yield_disc import YieldDiscRequest
		return YieldDiscRequest(self.request_adapter, path_parameters)

	def yield_mat(self,
		drive_id: str,
		driveItem_id: str,
	) -> YieldMatRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .yield_mat import YieldMatRequest
		return YieldMatRequest(self.request_adapter, path_parameters)

	def z__test(self,
		drive_id: str,
		driveItem_id: str,
	) -> Z_TestRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .z__test import Z_TestRequest
		return Z_TestRequest(self.request_adapter, path_parameters)

