import typing_extensions

from workday_staffing_python_sdk.paths import PathValues
from workday_staffing_python_sdk.apis.paths.job_changes_id_location import JobChangesIDLocation
from workday_staffing_python_sdk.apis.paths.workers_id_organization_assignment_changes import WorkersIDOrganizationAssignmentChanges
from workday_staffing_python_sdk.apis.paths.workers_id_skill_items import WorkersIDSkillItems
from workday_staffing_python_sdk.apis.paths.job_changes_id_start_details_subresource_id import JobChangesIDStartDetailsSubresourceID
from workday_staffing_python_sdk.apis.paths.organization_assignment_changes_id_region import OrganizationAssignmentChangesIDRegion
from workday_staffing_python_sdk.apis.paths.workers_id_work_contact_information_changes import WorkersIDWorkContactInformationChanges
from workday_staffing_python_sdk.apis.paths.job_changes_id_administrative import JobChangesIDAdministrative
from workday_staffing_python_sdk.apis.paths.job_changes_id_job_profile_subresource_id import JobChangesIDJobProfileSubresourceID
from workday_staffing_python_sdk.apis.paths.job_changes_id_location_subresource_id import JobChangesIDLocationSubresourceID
from workday_staffing_python_sdk.apis.paths.workers_id_check_in_topics import WorkersIDCheckInTopics
from workday_staffing_python_sdk.apis.paths.organization_assignment_changes_id_comment import OrganizationAssignmentChangesIDComment
from workday_staffing_python_sdk.apis.paths.organization_assignment_changes_id import OrganizationAssignmentChangesID
from workday_staffing_python_sdk.apis.paths.organization_assignment_changes_id_custom_organizations_subresource_id import OrganizationAssignmentChangesIDCustomOrganizationsSubresourceID
from workday_staffing_python_sdk.apis.paths.organization_assignment_changes_id_business_unit_subresource_id import OrganizationAssignmentChangesIDBusinessUnitSubresourceID
from workday_staffing_python_sdk.apis.paths.supervisory_organizations_id import SupervisoryOrganizationsID
from workday_staffing_python_sdk.apis.paths.job_changes_id_position import JobChangesIDPosition
from workday_staffing_python_sdk.apis.paths.job_changes_id_start_details import JobChangesIDStartDetails
from workday_staffing_python_sdk.apis.paths.supervisory_organizations_id_org_chart import SupervisoryOrganizationsIDOrgChart
from workday_staffing_python_sdk.apis.paths.workers_id_check_in_topics_subresource_i_dtypearchive import WorkersIDCheckInTopicsSubresourceIDtypearchive
from workday_staffing_python_sdk.apis.paths.workers_id_skill_items_subresource_id import WorkersIDSkillItemsSubresourceID
from workday_staffing_python_sdk.apis.paths.workers_id_external_skill_level_subresource_id import WorkersIDExternalSkillLevelSubresourceID
from workday_staffing_python_sdk.apis.paths.organization_assignment_changes_id_start_details_subresource_id import OrganizationAssignmentChangesIDStartDetailsSubresourceID
from workday_staffing_python_sdk.apis.paths.job_changes_id_move_team_subresource_id import JobChangesIDMoveTeamSubresourceID
from workday_staffing_python_sdk.apis.paths.workers_id_home_contact_information_changes import WorkersIDHomeContactInformationChanges
from workday_staffing_python_sdk.apis.paths.job_changes_id_position_subresource_id import JobChangesIDPositionSubresourceID
from workday_staffing_python_sdk.apis.paths.job_changes_id_comment import JobChangesIDComment
from workday_staffing_python_sdk.apis.paths.job_profiles import JobProfiles
from workday_staffing_python_sdk.apis.paths.job_changes_id_business_title_subresource_id import JobChangesIDBusinessTitleSubresourceID
from workday_staffing_python_sdk.apis.paths.workers_id_check_ins_subresource_id import WorkersIDCheckInsSubresourceID
from workday_staffing_python_sdk.apis.paths.job_changes_id_job_classification import JobChangesIDJobClassification
from workday_staffing_python_sdk.apis.paths.job_changes_id_administrative_subresource_id import JobChangesIDAdministrativeSubresourceID
from workday_staffing_python_sdk.apis.paths.job_changes_id_move_team import JobChangesIDMoveTeam
from workday_staffing_python_sdk.apis.paths.job_changes_id_opening import JobChangesIDOpening
from workday_staffing_python_sdk.apis.paths.workers_id_explicit_skills import WorkersIDExplicitSkills
from workday_staffing_python_sdk.apis.paths.job_changes_id_business_title import JobChangesIDBusinessTitle
from workday_staffing_python_sdk.apis.paths.workers_id_explicit_skills_subresource_id import WorkersIDExplicitSkillsSubresourceID
from workday_staffing_python_sdk.apis.paths.organization_assignment_changes_id_company_subresource_id import OrganizationAssignmentChangesIDCompanySubresourceID
from workday_staffing_python_sdk.apis.paths.job_families import JobFamilies
from workday_staffing_python_sdk.apis.paths.organization_assignment_changes_id_costing_subresource_id import OrganizationAssignmentChangesIDCostingSubresourceID
from workday_staffing_python_sdk.apis.paths.workers_id_check_in_topics_subresource_id import WorkersIDCheckInTopicsSubresourceID
from workday_staffing_python_sdk.apis.paths.workers_id_home_contact_information_changes_subresource_id import WorkersIDHomeContactInformationChangesSubresourceID
from workday_staffing_python_sdk.apis.paths.jobs_id_workspace import JobsIDWorkspace
from workday_staffing_python_sdk.apis.paths.job_changes_id_contract import JobChangesIDContract
from workday_staffing_python_sdk.apis.paths.organization_assignment_changes_id_start_details import OrganizationAssignmentChangesIDStartDetails
from workday_staffing_python_sdk.apis.paths.organization_assignment_changes_id_region_subresource_id import OrganizationAssignmentChangesIDRegionSubresourceID
from workday_staffing_python_sdk.apis.paths.workers_id_work_contact_information_changes_subresource_id import WorkersIDWorkContactInformationChangesSubresourceID
from workday_staffing_python_sdk.apis.paths.jobs_id import JobsID
from workday_staffing_python_sdk.apis.paths.job_changes_id import JobChangesID
from workday_staffing_python_sdk.apis.paths.workers_id_check_ins import WorkersIDCheckIns
from workday_staffing_python_sdk.apis.paths.workers import Workers
from workday_staffing_python_sdk.apis.paths.job_families_id import JobFamiliesID
from workday_staffing_python_sdk.apis.paths.organization_assignment_changes_id_custom_organizations import OrganizationAssignmentChangesIDCustomOrganizations
from workday_staffing_python_sdk.apis.paths.job_changes_id_submit import JobChangesIDSubmit
from workday_staffing_python_sdk.apis.paths.job_changes_id_job_classification_subresource_id import JobChangesIDJobClassificationSubresourceID
from workday_staffing_python_sdk.apis.paths.supervisory_organizations_id_members_subresource_id import SupervisoryOrganizationsIDMembersSubresourceID
from workday_staffing_python_sdk.apis.paths.workers_id_job_changes import WorkersIDJobChanges
from workday_staffing_python_sdk.apis.paths.job_changes_id_opening_subresource_id import JobChangesIDOpeningSubresourceID
from workday_staffing_python_sdk.apis.paths.supervisory_organizations import SupervisoryOrganizations
from workday_staffing_python_sdk.apis.paths.organization_assignment_changes_id_costing import OrganizationAssignmentChangesIDCosting
from workday_staffing_python_sdk.apis.paths.workers_id import WorkersID
from workday_staffing_python_sdk.apis.paths.workers_id_service_dates_subresource_id import WorkersIDServiceDatesSubresourceID
from workday_staffing_python_sdk.apis.paths.organization_assignment_changes_id_submit import OrganizationAssignmentChangesIDSubmit
from workday_staffing_python_sdk.apis.paths.organization_assignment_changes_id_cost_center_subresource_id import OrganizationAssignmentChangesIDCostCenterSubresourceID
from workday_staffing_python_sdk.apis.paths.organization_assignment_changes_id_comment_subresource_id import OrganizationAssignmentChangesIDCommentSubresourceID
from workday_staffing_python_sdk.apis.paths.workers_id_service_dates import WorkersIDServiceDates
from workday_staffing_python_sdk.apis.paths.job_changes_id_contract_subresource_id import JobChangesIDContractSubresourceID
from workday_staffing_python_sdk.apis.paths.jobs import Jobs
from workday_staffing_python_sdk.apis.paths.workers_id_check_ins_subresource_i_dtypearchive import WorkersIDCheckInsSubresourceIDtypearchive
from workday_staffing_python_sdk.apis.paths.job_changes_id_job_profile import JobChangesIDJobProfile
from workday_staffing_python_sdk.apis.paths.job_profiles_id import JobProfilesID
from workday_staffing_python_sdk.apis.paths.workers_id_external_skill_level import WorkersIDExternalSkillLevel
from workday_staffing_python_sdk.apis.paths.organization_assignment_changes import OrganizationAssignmentChanges
from workday_staffing_python_sdk.apis.paths.supervisory_organizations_id_members import SupervisoryOrganizationsIDMembers
from workday_staffing_python_sdk.apis.paths.jobs_id_workspace_subresource_id import JobsIDWorkspaceSubresourceID
from workday_staffing_python_sdk.apis.paths.organization_assignment_changes_id_business_unit import OrganizationAssignmentChangesIDBusinessUnit
from workday_staffing_python_sdk.apis.paths.organization_assignment_changes_id_company import OrganizationAssignmentChangesIDCompany
from workday_staffing_python_sdk.apis.paths.supervisory_organizations_id_org_chart_subresource_id import SupervisoryOrganizationsIDOrgChartSubresourceID
from workday_staffing_python_sdk.apis.paths.job_changes_id_comment_subresource_id import JobChangesIDCommentSubresourceID
from workday_staffing_python_sdk.apis.paths.organization_assignment_changes_id_cost_center import OrganizationAssignmentChangesIDCostCenter
from workday_staffing_python_sdk.apis.paths.values_organization_assignment_changes_group_regions import ValuesOrganizationAssignmentChangesGroupRegions
from workday_staffing_python_sdk.apis.paths.values_job_changes_group_reason import ValuesJobChangesGroupReason
from workday_staffing_python_sdk.apis.paths.values_organization_assignment_changes_group_customs import ValuesOrganizationAssignmentChangesGroupCustoms
from workday_staffing_python_sdk.apis.paths.values_job_changes_group_supervisory_organization import ValuesJobChangesGroupSupervisoryOrganization
from workday_staffing_python_sdk.apis.paths.values_organization_assignment_changes_group_programs import ValuesOrganizationAssignmentChangesGroupPrograms
from workday_staffing_python_sdk.apis.paths.values_organization_assignment_changes_group_jobs import ValuesOrganizationAssignmentChangesGroupJobs
from workday_staffing_python_sdk.apis.paths.values_organization_assignment_changes_group_funds import ValuesOrganizationAssignmentChangesGroupFunds
from workday_staffing_python_sdk.apis.paths.values_job_changes_group_workers_compensation_code_overrides import ValuesJobChangesGroupWorkersCompensationCodeOverrides
from workday_staffing_python_sdk.apis.paths.values_job_changes_group_time_types import ValuesJobChangesGroupTimeTypes
from workday_staffing_python_sdk.apis.paths.values_job_changes_group_work_shifts import ValuesJobChangesGroupWorkShifts
from workday_staffing_python_sdk.apis.paths.values_organization_assignment_changes_group_cost_centers import ValuesOrganizationAssignmentChangesGroupCostCenters
from workday_staffing_python_sdk.apis.paths.values_organization_assignment_changes_group_business_units import ValuesOrganizationAssignmentChangesGroupBusinessUnits
from workday_staffing_python_sdk.apis.paths.values_job_changes_group_frequencies import ValuesJobChangesGroupFrequencies
from workday_staffing_python_sdk.apis.paths.values_job_changes_group_employee_types import ValuesJobChangesGroupEmployeeTypes
from workday_staffing_python_sdk.apis.paths.values_job_changes_group_pay_rate_types import ValuesJobChangesGroupPayRateTypes
from workday_staffing_python_sdk.apis.paths.values_job_changes_group_templates import ValuesJobChangesGroupTemplates
from workday_staffing_python_sdk.apis.paths.values_job_changes_group_workers import ValuesJobChangesGroupWorkers
from workday_staffing_python_sdk.apis.paths.values_job_changes_group_contingent_worker_types import ValuesJobChangesGroupContingentWorkerTypes
from workday_staffing_python_sdk.apis.paths.values_job_changes_group_currencies import ValuesJobChangesGroupCurrencies
from workday_staffing_python_sdk.apis.paths.values_job_changes_group_proposed_position import ValuesJobChangesGroupProposedPosition
from workday_staffing_python_sdk.apis.paths.values_job_changes_group_jobs import ValuesJobChangesGroupJobs
from workday_staffing_python_sdk.apis.paths.values_job_changes_group_company_insider_types import ValuesJobChangesGroupCompanyInsiderTypes
from workday_staffing_python_sdk.apis.paths.values_job_changes_group_headcount_options import ValuesJobChangesGroupHeadcountOptions
from workday_staffing_python_sdk.apis.paths.values_organization_assignment_changes_group_grants import ValuesOrganizationAssignmentChangesGroupGrants
from workday_staffing_python_sdk.apis.paths.values_job_changes_group_worker_types import ValuesJobChangesGroupWorkerTypes
from workday_staffing_python_sdk.apis.paths.values_organization_assignment_changes_group_workers import ValuesOrganizationAssignmentChangesGroupWorkers
from workday_staffing_python_sdk.apis.paths.values_job_changes_group_work_study_awards import ValuesJobChangesGroupWorkStudyAwards
from workday_staffing_python_sdk.apis.paths.values_job_changes_group_locations import ValuesJobChangesGroupLocations
from workday_staffing_python_sdk.apis.paths.values_organization_assignment_changes_group_positions import ValuesOrganizationAssignmentChangesGroupPositions
from workday_staffing_python_sdk.apis.paths.values_job_changes_group_job_requisitions import ValuesJobChangesGroupJobRequisitions
from workday_staffing_python_sdk.apis.paths.values_job_changes_group_job_profiles import ValuesJobChangesGroupJobProfiles
from workday_staffing_python_sdk.apis.paths.values_organization_assignment_changes_group_companies import ValuesOrganizationAssignmentChangesGroupCompanies
from workday_staffing_python_sdk.apis.paths.values_job_changes_group_work_spaces import ValuesJobChangesGroupWorkSpaces
from workday_staffing_python_sdk.apis.paths.values_job_changes_group_assignment_types import ValuesJobChangesGroupAssignmentTypes
from workday_staffing_python_sdk.apis.paths.values_job_changes_group_job_classifications import ValuesJobChangesGroupJobClassifications
from workday_staffing_python_sdk.apis.paths.values_organization_assignment_changes_group_gifts import ValuesOrganizationAssignmentChangesGroupGifts

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.JOB_CHANGES_ID_LOCATION: JobChangesIDLocation,
        PathValues.WORKERS_ID_ORGANIZATION_ASSIGNMENT_CHANGES: WorkersIDOrganizationAssignmentChanges,
        PathValues.WORKERS_ID_SKILL_ITEMS: WorkersIDSkillItems,
        PathValues.JOB_CHANGES_ID_START_DETAILS_SUBRESOURCE_ID: JobChangesIDStartDetailsSubresourceID,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_REGION: OrganizationAssignmentChangesIDRegion,
        PathValues.WORKERS_ID_WORK_CONTACT_INFORMATION_CHANGES: WorkersIDWorkContactInformationChanges,
        PathValues.JOB_CHANGES_ID_ADMINISTRATIVE: JobChangesIDAdministrative,
        PathValues.JOB_CHANGES_ID_JOB_PROFILE_SUBRESOURCE_ID: JobChangesIDJobProfileSubresourceID,
        PathValues.JOB_CHANGES_ID_LOCATION_SUBRESOURCE_ID: JobChangesIDLocationSubresourceID,
        PathValues.WORKERS_ID_CHECK_IN_TOPICS: WorkersIDCheckInTopics,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_COMMENT: OrganizationAssignmentChangesIDComment,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID: OrganizationAssignmentChangesID,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_CUSTOM_ORGANIZATIONS_SUBRESOURCE_ID: OrganizationAssignmentChangesIDCustomOrganizationsSubresourceID,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_BUSINESS_UNIT_SUBRESOURCE_ID: OrganizationAssignmentChangesIDBusinessUnitSubresourceID,
        PathValues.SUPERVISORY_ORGANIZATIONS_ID: SupervisoryOrganizationsID,
        PathValues.JOB_CHANGES_ID_POSITION: JobChangesIDPosition,
        PathValues.JOB_CHANGES_ID_START_DETAILS: JobChangesIDStartDetails,
        PathValues.SUPERVISORY_ORGANIZATIONS_ID_ORG_CHART: SupervisoryOrganizationsIDOrgChart,
        PathValues.WORKERS_ID_CHECK_IN_TOPICS_SUBRESOURCE_IDTYPEARCHIVE: WorkersIDCheckInTopicsSubresourceIDtypearchive,
        PathValues.WORKERS_ID_SKILL_ITEMS_SUBRESOURCE_ID: WorkersIDSkillItemsSubresourceID,
        PathValues.WORKERS_ID_EXTERNAL_SKILL_LEVEL_SUBRESOURCE_ID: WorkersIDExternalSkillLevelSubresourceID,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_START_DETAILS_SUBRESOURCE_ID: OrganizationAssignmentChangesIDStartDetailsSubresourceID,
        PathValues.JOB_CHANGES_ID_MOVE_TEAM_SUBRESOURCE_ID: JobChangesIDMoveTeamSubresourceID,
        PathValues.WORKERS_ID_HOME_CONTACT_INFORMATION_CHANGES: WorkersIDHomeContactInformationChanges,
        PathValues.JOB_CHANGES_ID_POSITION_SUBRESOURCE_ID: JobChangesIDPositionSubresourceID,
        PathValues.JOB_CHANGES_ID_COMMENT: JobChangesIDComment,
        PathValues.JOB_PROFILES: JobProfiles,
        PathValues.JOB_CHANGES_ID_BUSINESS_TITLE_SUBRESOURCE_ID: JobChangesIDBusinessTitleSubresourceID,
        PathValues.WORKERS_ID_CHECK_INS_SUBRESOURCE_ID: WorkersIDCheckInsSubresourceID,
        PathValues.JOB_CHANGES_ID_JOB_CLASSIFICATION: JobChangesIDJobClassification,
        PathValues.JOB_CHANGES_ID_ADMINISTRATIVE_SUBRESOURCE_ID: JobChangesIDAdministrativeSubresourceID,
        PathValues.JOB_CHANGES_ID_MOVE_TEAM: JobChangesIDMoveTeam,
        PathValues.JOB_CHANGES_ID_OPENING: JobChangesIDOpening,
        PathValues.WORKERS_ID_EXPLICIT_SKILLS: WorkersIDExplicitSkills,
        PathValues.JOB_CHANGES_ID_BUSINESS_TITLE: JobChangesIDBusinessTitle,
        PathValues.WORKERS_ID_EXPLICIT_SKILLS_SUBRESOURCE_ID: WorkersIDExplicitSkillsSubresourceID,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_COMPANY_SUBRESOURCE_ID: OrganizationAssignmentChangesIDCompanySubresourceID,
        PathValues.JOB_FAMILIES: JobFamilies,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_COSTING_SUBRESOURCE_ID: OrganizationAssignmentChangesIDCostingSubresourceID,
        PathValues.WORKERS_ID_CHECK_IN_TOPICS_SUBRESOURCE_ID: WorkersIDCheckInTopicsSubresourceID,
        PathValues.WORKERS_ID_HOME_CONTACT_INFORMATION_CHANGES_SUBRESOURCE_ID: WorkersIDHomeContactInformationChangesSubresourceID,
        PathValues.JOBS_ID_WORKSPACE: JobsIDWorkspace,
        PathValues.JOB_CHANGES_ID_CONTRACT: JobChangesIDContract,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_START_DETAILS: OrganizationAssignmentChangesIDStartDetails,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_REGION_SUBRESOURCE_ID: OrganizationAssignmentChangesIDRegionSubresourceID,
        PathValues.WORKERS_ID_WORK_CONTACT_INFORMATION_CHANGES_SUBRESOURCE_ID: WorkersIDWorkContactInformationChangesSubresourceID,
        PathValues.JOBS_ID: JobsID,
        PathValues.JOB_CHANGES_ID: JobChangesID,
        PathValues.WORKERS_ID_CHECK_INS: WorkersIDCheckIns,
        PathValues.WORKERS: Workers,
        PathValues.JOB_FAMILIES_ID: JobFamiliesID,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_CUSTOM_ORGANIZATIONS: OrganizationAssignmentChangesIDCustomOrganizations,
        PathValues.JOB_CHANGES_ID_SUBMIT: JobChangesIDSubmit,
        PathValues.JOB_CHANGES_ID_JOB_CLASSIFICATION_SUBRESOURCE_ID: JobChangesIDJobClassificationSubresourceID,
        PathValues.SUPERVISORY_ORGANIZATIONS_ID_MEMBERS_SUBRESOURCE_ID: SupervisoryOrganizationsIDMembersSubresourceID,
        PathValues.WORKERS_ID_JOB_CHANGES: WorkersIDJobChanges,
        PathValues.JOB_CHANGES_ID_OPENING_SUBRESOURCE_ID: JobChangesIDOpeningSubresourceID,
        PathValues.SUPERVISORY_ORGANIZATIONS: SupervisoryOrganizations,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_COSTING: OrganizationAssignmentChangesIDCosting,
        PathValues.WORKERS_ID: WorkersID,
        PathValues.WORKERS_ID_SERVICE_DATES_SUBRESOURCE_ID: WorkersIDServiceDatesSubresourceID,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_SUBMIT: OrganizationAssignmentChangesIDSubmit,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_COST_CENTER_SUBRESOURCE_ID: OrganizationAssignmentChangesIDCostCenterSubresourceID,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_COMMENT_SUBRESOURCE_ID: OrganizationAssignmentChangesIDCommentSubresourceID,
        PathValues.WORKERS_ID_SERVICE_DATES: WorkersIDServiceDates,
        PathValues.JOB_CHANGES_ID_CONTRACT_SUBRESOURCE_ID: JobChangesIDContractSubresourceID,
        PathValues.JOBS: Jobs,
        PathValues.WORKERS_ID_CHECK_INS_SUBRESOURCE_IDTYPEARCHIVE: WorkersIDCheckInsSubresourceIDtypearchive,
        PathValues.JOB_CHANGES_ID_JOB_PROFILE: JobChangesIDJobProfile,
        PathValues.JOB_PROFILES_ID: JobProfilesID,
        PathValues.WORKERS_ID_EXTERNAL_SKILL_LEVEL: WorkersIDExternalSkillLevel,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES: OrganizationAssignmentChanges,
        PathValues.SUPERVISORY_ORGANIZATIONS_ID_MEMBERS: SupervisoryOrganizationsIDMembers,
        PathValues.JOBS_ID_WORKSPACE_SUBRESOURCE_ID: JobsIDWorkspaceSubresourceID,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_BUSINESS_UNIT: OrganizationAssignmentChangesIDBusinessUnit,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_COMPANY: OrganizationAssignmentChangesIDCompany,
        PathValues.SUPERVISORY_ORGANIZATIONS_ID_ORG_CHART_SUBRESOURCE_ID: SupervisoryOrganizationsIDOrgChartSubresourceID,
        PathValues.JOB_CHANGES_ID_COMMENT_SUBRESOURCE_ID: JobChangesIDCommentSubresourceID,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_COST_CENTER: OrganizationAssignmentChangesIDCostCenter,
        PathValues.VALUES_ORGANIZATION_ASSIGNMENT_CHANGES_GROUP_REGIONS: ValuesOrganizationAssignmentChangesGroupRegions,
        PathValues.VALUES_JOB_CHANGES_GROUP_REASON: ValuesJobChangesGroupReason,
        PathValues.VALUES_ORGANIZATION_ASSIGNMENT_CHANGES_GROUP_CUSTOMS: ValuesOrganizationAssignmentChangesGroupCustoms,
        PathValues.VALUES_JOB_CHANGES_GROUP_SUPERVISORY_ORGANIZATION: ValuesJobChangesGroupSupervisoryOrganization,
        PathValues.VALUES_ORGANIZATION_ASSIGNMENT_CHANGES_GROUP_PROGRAMS: ValuesOrganizationAssignmentChangesGroupPrograms,
        PathValues.VALUES_ORGANIZATION_ASSIGNMENT_CHANGES_GROUP_JOBS: ValuesOrganizationAssignmentChangesGroupJobs,
        PathValues.VALUES_ORGANIZATION_ASSIGNMENT_CHANGES_GROUP_FUNDS: ValuesOrganizationAssignmentChangesGroupFunds,
        PathValues.VALUES_JOB_CHANGES_GROUP_WORKERS_COMPENSATION_CODE_OVERRIDES: ValuesJobChangesGroupWorkersCompensationCodeOverrides,
        PathValues.VALUES_JOB_CHANGES_GROUP_TIME_TYPES: ValuesJobChangesGroupTimeTypes,
        PathValues.VALUES_JOB_CHANGES_GROUP_WORK_SHIFTS: ValuesJobChangesGroupWorkShifts,
        PathValues.VALUES_ORGANIZATION_ASSIGNMENT_CHANGES_GROUP_COST_CENTERS: ValuesOrganizationAssignmentChangesGroupCostCenters,
        PathValues.VALUES_ORGANIZATION_ASSIGNMENT_CHANGES_GROUP_BUSINESS_UNITS: ValuesOrganizationAssignmentChangesGroupBusinessUnits,
        PathValues.VALUES_JOB_CHANGES_GROUP_FREQUENCIES: ValuesJobChangesGroupFrequencies,
        PathValues.VALUES_JOB_CHANGES_GROUP_EMPLOYEE_TYPES: ValuesJobChangesGroupEmployeeTypes,
        PathValues.VALUES_JOB_CHANGES_GROUP_PAY_RATE_TYPES: ValuesJobChangesGroupPayRateTypes,
        PathValues.VALUES_JOB_CHANGES_GROUP_TEMPLATES: ValuesJobChangesGroupTemplates,
        PathValues.VALUES_JOB_CHANGES_GROUP_WORKERS: ValuesJobChangesGroupWorkers,
        PathValues.VALUES_JOB_CHANGES_GROUP_CONTINGENT_WORKER_TYPES: ValuesJobChangesGroupContingentWorkerTypes,
        PathValues.VALUES_JOB_CHANGES_GROUP_CURRENCIES: ValuesJobChangesGroupCurrencies,
        PathValues.VALUES_JOB_CHANGES_GROUP_PROPOSED_POSITION: ValuesJobChangesGroupProposedPosition,
        PathValues.VALUES_JOB_CHANGES_GROUP_JOBS: ValuesJobChangesGroupJobs,
        PathValues.VALUES_JOB_CHANGES_GROUP_COMPANY_INSIDER_TYPES: ValuesJobChangesGroupCompanyInsiderTypes,
        PathValues.VALUES_JOB_CHANGES_GROUP_HEADCOUNT_OPTIONS: ValuesJobChangesGroupHeadcountOptions,
        PathValues.VALUES_ORGANIZATION_ASSIGNMENT_CHANGES_GROUP_GRANTS: ValuesOrganizationAssignmentChangesGroupGrants,
        PathValues.VALUES_JOB_CHANGES_GROUP_WORKER_TYPES: ValuesJobChangesGroupWorkerTypes,
        PathValues.VALUES_ORGANIZATION_ASSIGNMENT_CHANGES_GROUP_WORKERS: ValuesOrganizationAssignmentChangesGroupWorkers,
        PathValues.VALUES_JOB_CHANGES_GROUP_WORK_STUDY_AWARDS: ValuesJobChangesGroupWorkStudyAwards,
        PathValues.VALUES_JOB_CHANGES_GROUP_LOCATIONS: ValuesJobChangesGroupLocations,
        PathValues.VALUES_ORGANIZATION_ASSIGNMENT_CHANGES_GROUP_POSITIONS: ValuesOrganizationAssignmentChangesGroupPositions,
        PathValues.VALUES_JOB_CHANGES_GROUP_JOB_REQUISITIONS: ValuesJobChangesGroupJobRequisitions,
        PathValues.VALUES_JOB_CHANGES_GROUP_JOB_PROFILES: ValuesJobChangesGroupJobProfiles,
        PathValues.VALUES_ORGANIZATION_ASSIGNMENT_CHANGES_GROUP_COMPANIES: ValuesOrganizationAssignmentChangesGroupCompanies,
        PathValues.VALUES_JOB_CHANGES_GROUP_WORK_SPACES: ValuesJobChangesGroupWorkSpaces,
        PathValues.VALUES_JOB_CHANGES_GROUP_ASSIGNMENT_TYPES: ValuesJobChangesGroupAssignmentTypes,
        PathValues.VALUES_JOB_CHANGES_GROUP_JOB_CLASSIFICATIONS: ValuesJobChangesGroupJobClassifications,
        PathValues.VALUES_ORGANIZATION_ASSIGNMENT_CHANGES_GROUP_GIFTS: ValuesOrganizationAssignmentChangesGroupGifts,
    }
)

path_to_api = PathToApi(
    {
        PathValues.JOB_CHANGES_ID_LOCATION: JobChangesIDLocation,
        PathValues.WORKERS_ID_ORGANIZATION_ASSIGNMENT_CHANGES: WorkersIDOrganizationAssignmentChanges,
        PathValues.WORKERS_ID_SKILL_ITEMS: WorkersIDSkillItems,
        PathValues.JOB_CHANGES_ID_START_DETAILS_SUBRESOURCE_ID: JobChangesIDStartDetailsSubresourceID,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_REGION: OrganizationAssignmentChangesIDRegion,
        PathValues.WORKERS_ID_WORK_CONTACT_INFORMATION_CHANGES: WorkersIDWorkContactInformationChanges,
        PathValues.JOB_CHANGES_ID_ADMINISTRATIVE: JobChangesIDAdministrative,
        PathValues.JOB_CHANGES_ID_JOB_PROFILE_SUBRESOURCE_ID: JobChangesIDJobProfileSubresourceID,
        PathValues.JOB_CHANGES_ID_LOCATION_SUBRESOURCE_ID: JobChangesIDLocationSubresourceID,
        PathValues.WORKERS_ID_CHECK_IN_TOPICS: WorkersIDCheckInTopics,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_COMMENT: OrganizationAssignmentChangesIDComment,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID: OrganizationAssignmentChangesID,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_CUSTOM_ORGANIZATIONS_SUBRESOURCE_ID: OrganizationAssignmentChangesIDCustomOrganizationsSubresourceID,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_BUSINESS_UNIT_SUBRESOURCE_ID: OrganizationAssignmentChangesIDBusinessUnitSubresourceID,
        PathValues.SUPERVISORY_ORGANIZATIONS_ID: SupervisoryOrganizationsID,
        PathValues.JOB_CHANGES_ID_POSITION: JobChangesIDPosition,
        PathValues.JOB_CHANGES_ID_START_DETAILS: JobChangesIDStartDetails,
        PathValues.SUPERVISORY_ORGANIZATIONS_ID_ORG_CHART: SupervisoryOrganizationsIDOrgChart,
        PathValues.WORKERS_ID_CHECK_IN_TOPICS_SUBRESOURCE_IDTYPEARCHIVE: WorkersIDCheckInTopicsSubresourceIDtypearchive,
        PathValues.WORKERS_ID_SKILL_ITEMS_SUBRESOURCE_ID: WorkersIDSkillItemsSubresourceID,
        PathValues.WORKERS_ID_EXTERNAL_SKILL_LEVEL_SUBRESOURCE_ID: WorkersIDExternalSkillLevelSubresourceID,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_START_DETAILS_SUBRESOURCE_ID: OrganizationAssignmentChangesIDStartDetailsSubresourceID,
        PathValues.JOB_CHANGES_ID_MOVE_TEAM_SUBRESOURCE_ID: JobChangesIDMoveTeamSubresourceID,
        PathValues.WORKERS_ID_HOME_CONTACT_INFORMATION_CHANGES: WorkersIDHomeContactInformationChanges,
        PathValues.JOB_CHANGES_ID_POSITION_SUBRESOURCE_ID: JobChangesIDPositionSubresourceID,
        PathValues.JOB_CHANGES_ID_COMMENT: JobChangesIDComment,
        PathValues.JOB_PROFILES: JobProfiles,
        PathValues.JOB_CHANGES_ID_BUSINESS_TITLE_SUBRESOURCE_ID: JobChangesIDBusinessTitleSubresourceID,
        PathValues.WORKERS_ID_CHECK_INS_SUBRESOURCE_ID: WorkersIDCheckInsSubresourceID,
        PathValues.JOB_CHANGES_ID_JOB_CLASSIFICATION: JobChangesIDJobClassification,
        PathValues.JOB_CHANGES_ID_ADMINISTRATIVE_SUBRESOURCE_ID: JobChangesIDAdministrativeSubresourceID,
        PathValues.JOB_CHANGES_ID_MOVE_TEAM: JobChangesIDMoveTeam,
        PathValues.JOB_CHANGES_ID_OPENING: JobChangesIDOpening,
        PathValues.WORKERS_ID_EXPLICIT_SKILLS: WorkersIDExplicitSkills,
        PathValues.JOB_CHANGES_ID_BUSINESS_TITLE: JobChangesIDBusinessTitle,
        PathValues.WORKERS_ID_EXPLICIT_SKILLS_SUBRESOURCE_ID: WorkersIDExplicitSkillsSubresourceID,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_COMPANY_SUBRESOURCE_ID: OrganizationAssignmentChangesIDCompanySubresourceID,
        PathValues.JOB_FAMILIES: JobFamilies,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_COSTING_SUBRESOURCE_ID: OrganizationAssignmentChangesIDCostingSubresourceID,
        PathValues.WORKERS_ID_CHECK_IN_TOPICS_SUBRESOURCE_ID: WorkersIDCheckInTopicsSubresourceID,
        PathValues.WORKERS_ID_HOME_CONTACT_INFORMATION_CHANGES_SUBRESOURCE_ID: WorkersIDHomeContactInformationChangesSubresourceID,
        PathValues.JOBS_ID_WORKSPACE: JobsIDWorkspace,
        PathValues.JOB_CHANGES_ID_CONTRACT: JobChangesIDContract,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_START_DETAILS: OrganizationAssignmentChangesIDStartDetails,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_REGION_SUBRESOURCE_ID: OrganizationAssignmentChangesIDRegionSubresourceID,
        PathValues.WORKERS_ID_WORK_CONTACT_INFORMATION_CHANGES_SUBRESOURCE_ID: WorkersIDWorkContactInformationChangesSubresourceID,
        PathValues.JOBS_ID: JobsID,
        PathValues.JOB_CHANGES_ID: JobChangesID,
        PathValues.WORKERS_ID_CHECK_INS: WorkersIDCheckIns,
        PathValues.WORKERS: Workers,
        PathValues.JOB_FAMILIES_ID: JobFamiliesID,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_CUSTOM_ORGANIZATIONS: OrganizationAssignmentChangesIDCustomOrganizations,
        PathValues.JOB_CHANGES_ID_SUBMIT: JobChangesIDSubmit,
        PathValues.JOB_CHANGES_ID_JOB_CLASSIFICATION_SUBRESOURCE_ID: JobChangesIDJobClassificationSubresourceID,
        PathValues.SUPERVISORY_ORGANIZATIONS_ID_MEMBERS_SUBRESOURCE_ID: SupervisoryOrganizationsIDMembersSubresourceID,
        PathValues.WORKERS_ID_JOB_CHANGES: WorkersIDJobChanges,
        PathValues.JOB_CHANGES_ID_OPENING_SUBRESOURCE_ID: JobChangesIDOpeningSubresourceID,
        PathValues.SUPERVISORY_ORGANIZATIONS: SupervisoryOrganizations,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_COSTING: OrganizationAssignmentChangesIDCosting,
        PathValues.WORKERS_ID: WorkersID,
        PathValues.WORKERS_ID_SERVICE_DATES_SUBRESOURCE_ID: WorkersIDServiceDatesSubresourceID,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_SUBMIT: OrganizationAssignmentChangesIDSubmit,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_COST_CENTER_SUBRESOURCE_ID: OrganizationAssignmentChangesIDCostCenterSubresourceID,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_COMMENT_SUBRESOURCE_ID: OrganizationAssignmentChangesIDCommentSubresourceID,
        PathValues.WORKERS_ID_SERVICE_DATES: WorkersIDServiceDates,
        PathValues.JOB_CHANGES_ID_CONTRACT_SUBRESOURCE_ID: JobChangesIDContractSubresourceID,
        PathValues.JOBS: Jobs,
        PathValues.WORKERS_ID_CHECK_INS_SUBRESOURCE_IDTYPEARCHIVE: WorkersIDCheckInsSubresourceIDtypearchive,
        PathValues.JOB_CHANGES_ID_JOB_PROFILE: JobChangesIDJobProfile,
        PathValues.JOB_PROFILES_ID: JobProfilesID,
        PathValues.WORKERS_ID_EXTERNAL_SKILL_LEVEL: WorkersIDExternalSkillLevel,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES: OrganizationAssignmentChanges,
        PathValues.SUPERVISORY_ORGANIZATIONS_ID_MEMBERS: SupervisoryOrganizationsIDMembers,
        PathValues.JOBS_ID_WORKSPACE_SUBRESOURCE_ID: JobsIDWorkspaceSubresourceID,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_BUSINESS_UNIT: OrganizationAssignmentChangesIDBusinessUnit,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_COMPANY: OrganizationAssignmentChangesIDCompany,
        PathValues.SUPERVISORY_ORGANIZATIONS_ID_ORG_CHART_SUBRESOURCE_ID: SupervisoryOrganizationsIDOrgChartSubresourceID,
        PathValues.JOB_CHANGES_ID_COMMENT_SUBRESOURCE_ID: JobChangesIDCommentSubresourceID,
        PathValues.ORGANIZATION_ASSIGNMENT_CHANGES_ID_COST_CENTER: OrganizationAssignmentChangesIDCostCenter,
        PathValues.VALUES_ORGANIZATION_ASSIGNMENT_CHANGES_GROUP_REGIONS: ValuesOrganizationAssignmentChangesGroupRegions,
        PathValues.VALUES_JOB_CHANGES_GROUP_REASON: ValuesJobChangesGroupReason,
        PathValues.VALUES_ORGANIZATION_ASSIGNMENT_CHANGES_GROUP_CUSTOMS: ValuesOrganizationAssignmentChangesGroupCustoms,
        PathValues.VALUES_JOB_CHANGES_GROUP_SUPERVISORY_ORGANIZATION: ValuesJobChangesGroupSupervisoryOrganization,
        PathValues.VALUES_ORGANIZATION_ASSIGNMENT_CHANGES_GROUP_PROGRAMS: ValuesOrganizationAssignmentChangesGroupPrograms,
        PathValues.VALUES_ORGANIZATION_ASSIGNMENT_CHANGES_GROUP_JOBS: ValuesOrganizationAssignmentChangesGroupJobs,
        PathValues.VALUES_ORGANIZATION_ASSIGNMENT_CHANGES_GROUP_FUNDS: ValuesOrganizationAssignmentChangesGroupFunds,
        PathValues.VALUES_JOB_CHANGES_GROUP_WORKERS_COMPENSATION_CODE_OVERRIDES: ValuesJobChangesGroupWorkersCompensationCodeOverrides,
        PathValues.VALUES_JOB_CHANGES_GROUP_TIME_TYPES: ValuesJobChangesGroupTimeTypes,
        PathValues.VALUES_JOB_CHANGES_GROUP_WORK_SHIFTS: ValuesJobChangesGroupWorkShifts,
        PathValues.VALUES_ORGANIZATION_ASSIGNMENT_CHANGES_GROUP_COST_CENTERS: ValuesOrganizationAssignmentChangesGroupCostCenters,
        PathValues.VALUES_ORGANIZATION_ASSIGNMENT_CHANGES_GROUP_BUSINESS_UNITS: ValuesOrganizationAssignmentChangesGroupBusinessUnits,
        PathValues.VALUES_JOB_CHANGES_GROUP_FREQUENCIES: ValuesJobChangesGroupFrequencies,
        PathValues.VALUES_JOB_CHANGES_GROUP_EMPLOYEE_TYPES: ValuesJobChangesGroupEmployeeTypes,
        PathValues.VALUES_JOB_CHANGES_GROUP_PAY_RATE_TYPES: ValuesJobChangesGroupPayRateTypes,
        PathValues.VALUES_JOB_CHANGES_GROUP_TEMPLATES: ValuesJobChangesGroupTemplates,
        PathValues.VALUES_JOB_CHANGES_GROUP_WORKERS: ValuesJobChangesGroupWorkers,
        PathValues.VALUES_JOB_CHANGES_GROUP_CONTINGENT_WORKER_TYPES: ValuesJobChangesGroupContingentWorkerTypes,
        PathValues.VALUES_JOB_CHANGES_GROUP_CURRENCIES: ValuesJobChangesGroupCurrencies,
        PathValues.VALUES_JOB_CHANGES_GROUP_PROPOSED_POSITION: ValuesJobChangesGroupProposedPosition,
        PathValues.VALUES_JOB_CHANGES_GROUP_JOBS: ValuesJobChangesGroupJobs,
        PathValues.VALUES_JOB_CHANGES_GROUP_COMPANY_INSIDER_TYPES: ValuesJobChangesGroupCompanyInsiderTypes,
        PathValues.VALUES_JOB_CHANGES_GROUP_HEADCOUNT_OPTIONS: ValuesJobChangesGroupHeadcountOptions,
        PathValues.VALUES_ORGANIZATION_ASSIGNMENT_CHANGES_GROUP_GRANTS: ValuesOrganizationAssignmentChangesGroupGrants,
        PathValues.VALUES_JOB_CHANGES_GROUP_WORKER_TYPES: ValuesJobChangesGroupWorkerTypes,
        PathValues.VALUES_ORGANIZATION_ASSIGNMENT_CHANGES_GROUP_WORKERS: ValuesOrganizationAssignmentChangesGroupWorkers,
        PathValues.VALUES_JOB_CHANGES_GROUP_WORK_STUDY_AWARDS: ValuesJobChangesGroupWorkStudyAwards,
        PathValues.VALUES_JOB_CHANGES_GROUP_LOCATIONS: ValuesJobChangesGroupLocations,
        PathValues.VALUES_ORGANIZATION_ASSIGNMENT_CHANGES_GROUP_POSITIONS: ValuesOrganizationAssignmentChangesGroupPositions,
        PathValues.VALUES_JOB_CHANGES_GROUP_JOB_REQUISITIONS: ValuesJobChangesGroupJobRequisitions,
        PathValues.VALUES_JOB_CHANGES_GROUP_JOB_PROFILES: ValuesJobChangesGroupJobProfiles,
        PathValues.VALUES_ORGANIZATION_ASSIGNMENT_CHANGES_GROUP_COMPANIES: ValuesOrganizationAssignmentChangesGroupCompanies,
        PathValues.VALUES_JOB_CHANGES_GROUP_WORK_SPACES: ValuesJobChangesGroupWorkSpaces,
        PathValues.VALUES_JOB_CHANGES_GROUP_ASSIGNMENT_TYPES: ValuesJobChangesGroupAssignmentTypes,
        PathValues.VALUES_JOB_CHANGES_GROUP_JOB_CLASSIFICATIONS: ValuesJobChangesGroupJobClassifications,
        PathValues.VALUES_ORGANIZATION_ASSIGNMENT_CHANGES_GROUP_GIFTS: ValuesOrganizationAssignmentChangesGroupGifts,
    }
)
