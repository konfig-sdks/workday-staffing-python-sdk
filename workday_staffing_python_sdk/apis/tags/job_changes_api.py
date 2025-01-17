# coding: utf-8

"""
    staffing

    The Staffing REST APIs enable you to get and manage staffing information, such as jobs, job families, job profiles, supervisory organizations, worker check-ins, and job changes. The Staffing service also includes the /workers resource to access staffing information for non-terminated workers.    Related Information: - Administrator Guide: Setup Considerations: Job Changes

    The version of the OpenAPI document: v6
    Generated by: https://konfigthis.com
"""

from workday_staffing_python_sdk.paths.job_changes_id_administrative_subresource_id.get import GetAdminOptions
from workday_staffing_python_sdk.paths.job_changes_id_administrative.get import GetAdministrativeOptions
from workday_staffing_python_sdk.paths.job_changes_id_business_title_subresource_id.get import GetBusinessTitle
from workday_staffing_python_sdk.paths.job_changes_id_business_title.get import GetBusinessTitle0
from workday_staffing_python_sdk.paths.job_changes_id.get import GetById
from workday_staffing_python_sdk.paths.job_changes_id_comment.get import GetCommentById
from workday_staffing_python_sdk.paths.job_changes_id_comment_subresource_id.get import GetCommentInfo
from workday_staffing_python_sdk.paths.job_changes_id_contract.get import GetContractOptions
from workday_staffing_python_sdk.paths.job_changes_id_contract_subresource_id.get import GetContractOptions0
from workday_staffing_python_sdk.paths.job_changes_id_job_classification.get import GetJobClassification
from workday_staffing_python_sdk.paths.job_changes_id_job_classification_subresource_id.get import GetJobClassification0
from workday_staffing_python_sdk.paths.job_changes_id_job_profile.get import GetJobProfile
from workday_staffing_python_sdk.paths.job_changes_id_location.get import GetLocationInfo
from workday_staffing_python_sdk.paths.job_changes_id_location_subresource_id.get import GetLocationInfo0
from workday_staffing_python_sdk.paths.job_changes_id_move_team_subresource_id.get import GetMoveTeamOption
from workday_staffing_python_sdk.paths.job_changes_id_move_team.get import GetMoveTeamOption0
from workday_staffing_python_sdk.paths.job_changes_id_opening.get import GetOpeningOptions
from workday_staffing_python_sdk.paths.job_changes_id_opening_subresource_id.get import GetOpeningOptions0
from workday_staffing_python_sdk.paths.job_changes_id_position.get import GetPositionById
from workday_staffing_python_sdk.paths.job_changes_id_position_subresource_id.get import GetPositionBySubresourceId
from workday_staffing_python_sdk.paths.job_changes_id_job_profile_subresource_id.get import GetProfile
from workday_staffing_python_sdk.paths.job_changes_id_start_details_subresource_id.get import GetStartDetails
from workday_staffing_python_sdk.paths.job_changes_id_start_details.get import GetStartDetails0
from workday_staffing_python_sdk.paths.job_changes_id_location_subresource_id.patch import PartialUpdateLocationOptions
from workday_staffing_python_sdk.paths.job_changes_id_contract_subresource_id.patch import PartiallyUpdateContractOptions
from workday_staffing_python_sdk.paths.job_changes_id_submit.post import SubmitChangeJob
from workday_staffing_python_sdk.paths.job_changes_id_administrative_subresource_id.patch import UpdateAdministrativeOptions
from workday_staffing_python_sdk.paths.job_changes_id_business_title_subresource_id.patch import UpdateBusinessTitleOptions
from workday_staffing_python_sdk.paths.job_changes_id_comment_subresource_id.patch import UpdateComment
from workday_staffing_python_sdk.paths.job_changes_id_job_classification_subresource_id.patch import UpdateJobClassificationOptions
from workday_staffing_python_sdk.paths.job_changes_id_job_profile_subresource_id.patch import UpdateJobProfileOptions
from workday_staffing_python_sdk.paths.job_changes_id_move_team_subresource_id.patch import UpdateMoveTeamOptions
from workday_staffing_python_sdk.paths.job_changes_id_opening_subresource_id.patch import UpdateOpeningOptions
from workday_staffing_python_sdk.paths.job_changes_id_position_subresource_id.patch import UpdatePositionOptions
from workday_staffing_python_sdk.paths.job_changes_id_start_details_subresource_id.patch import UpdateStartDetails
from workday_staffing_python_sdk.apis.tags.job_changes_api_raw import JobChangesApiRaw


class JobChangesApi(
    GetAdminOptions,
    GetAdministrativeOptions,
    GetBusinessTitle,
    GetBusinessTitle0,
    GetById,
    GetCommentById,
    GetCommentInfo,
    GetContractOptions,
    GetContractOptions0,
    GetJobClassification,
    GetJobClassification0,
    GetJobProfile,
    GetLocationInfo,
    GetLocationInfo0,
    GetMoveTeamOption,
    GetMoveTeamOption0,
    GetOpeningOptions,
    GetOpeningOptions0,
    GetPositionById,
    GetPositionBySubresourceId,
    GetProfile,
    GetStartDetails,
    GetStartDetails0,
    PartialUpdateLocationOptions,
    PartiallyUpdateContractOptions,
    SubmitChangeJob,
    UpdateAdministrativeOptions,
    UpdateBusinessTitleOptions,
    UpdateComment,
    UpdateJobClassificationOptions,
    UpdateJobProfileOptions,
    UpdateMoveTeamOptions,
    UpdateOpeningOptions,
    UpdatePositionOptions,
    UpdateStartDetails,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: JobChangesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = JobChangesApiRaw(api_client)
