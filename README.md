<div align="left">

[![Visit Workday](./header.png)](https://workday.com)

# Workday<a id="workday"></a>

The Staffing REST APIs enable you to get and manage staffing information, such as jobs, job families, job profiles, supervisory organizations, worker check-ins, and job changes. The Staffing service also includes the /workers resource to access staffing information for non-terminated workers.



Related Information:
- Administrator Guide: Setup Considerations: Job Changes


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`workdaystaffing.prompt_values.available_locations`](#workdaystaffingprompt_valuesavailable_locations)
  * [`workdaystaffing.prompt_values.get_assignment_change_group_cost_centers`](#workdaystaffingprompt_valuesget_assignment_change_group_cost_centers)
  * [`workdaystaffing.prompt_values.get_assignment_types`](#workdaystaffingprompt_valuesget_assignment_types)
  * [`workdaystaffing.prompt_values.get_company_insider_types`](#workdaystaffingprompt_valuesget_company_insider_types)
  * [`workdaystaffing.prompt_values.get_contingent_worker_types`](#workdaystaffingprompt_valuesget_contingent_worker_types)
  * [`workdaystaffing.prompt_values.get_currency_instances`](#workdaystaffingprompt_valuesget_currency_instances)
  * [`workdaystaffing.prompt_values.get_employee_types`](#workdaystaffingprompt_valuesget_employee_types)
  * [`workdaystaffing.prompt_values.get_gift_instances`](#workdaystaffingprompt_valuesget_gift_instances)
  * [`workdaystaffing.prompt_values.get_grants`](#workdaystaffingprompt_valuesget_grants)
  * [`workdaystaffing.prompt_values.get_instances`](#workdaystaffingprompt_valuesget_instances)
  * [`workdaystaffing.prompt_values.get_instances_0`](#workdaystaffingprompt_valuesget_instances_0)
  * [`workdaystaffing.prompt_values.get_instances_1`](#workdaystaffingprompt_valuesget_instances_1)
  * [`workdaystaffing.prompt_values.get_instances_10`](#workdaystaffingprompt_valuesget_instances_10)
  * [`workdaystaffing.prompt_values.get_instances_11`](#workdaystaffingprompt_valuesget_instances_11)
  * [`workdaystaffing.prompt_values.get_instances_12`](#workdaystaffingprompt_valuesget_instances_12)
  * [`workdaystaffing.prompt_values.get_instances_13`](#workdaystaffingprompt_valuesget_instances_13)
  * [`workdaystaffing.prompt_values.get_instances_14`](#workdaystaffingprompt_valuesget_instances_14)
  * [`workdaystaffing.prompt_values.get_instances_15`](#workdaystaffingprompt_valuesget_instances_15)
  * [`workdaystaffing.prompt_values.get_instances_16`](#workdaystaffingprompt_valuesget_instances_16)
  * [`workdaystaffing.prompt_values.get_instances_17`](#workdaystaffingprompt_valuesget_instances_17)
  * [`workdaystaffing.prompt_values.get_instances_18`](#workdaystaffingprompt_valuesget_instances_18)
  * [`workdaystaffing.prompt_values.get_instances_19`](#workdaystaffingprompt_valuesget_instances_19)
  * [`workdaystaffing.prompt_values.get_instances_2`](#workdaystaffingprompt_valuesget_instances_2)
  * [`workdaystaffing.prompt_values.get_instances_3`](#workdaystaffingprompt_valuesget_instances_3)
  * [`workdaystaffing.prompt_values.get_instances_4`](#workdaystaffingprompt_valuesget_instances_4)
  * [`workdaystaffing.prompt_values.get_instances_5`](#workdaystaffingprompt_valuesget_instances_5)
  * [`workdaystaffing.prompt_values.get_instances_6`](#workdaystaffingprompt_valuesget_instances_6)
  * [`workdaystaffing.prompt_values.get_instances_7`](#workdaystaffingprompt_valuesget_instances_7)
  * [`workdaystaffing.prompt_values.get_instances_8`](#workdaystaffingprompt_valuesget_instances_8)
  * [`workdaystaffing.prompt_values.get_instances_9`](#workdaystaffingprompt_valuesget_instances_9)
  * [`workdaystaffing.prompt_values.get_options`](#workdaystaffingprompt_valuesget_options)
  * [`workdaystaffing.prompt_values.get_proposed_positions`](#workdaystaffingprompt_valuesget_proposed_positions)
  * [`workdaystaffing.prompt_values.get_supervisory_org_values`](#workdaystaffingprompt_valuesget_supervisory_org_values)
  * [`workdaystaffing.prompt_values.get_time_types`](#workdaystaffingprompt_valuesget_time_types)
  * [`workdaystaffing.prompt_values.get_worker_types`](#workdaystaffingprompt_valuesget_worker_types)
  * [`workdaystaffing.prompt_values.get_workspace_instances`](#workdaystaffingprompt_valuesget_workspace_instances)
  * [`workdaystaffing.job_changes.get_admin_options`](#workdaystaffingjob_changesget_admin_options)
  * [`workdaystaffing.job_changes.get_administrative_options`](#workdaystaffingjob_changesget_administrative_options)
  * [`workdaystaffing.job_changes.get_business_title`](#workdaystaffingjob_changesget_business_title)
  * [`workdaystaffing.job_changes.get_business_title_0`](#workdaystaffingjob_changesget_business_title_0)
  * [`workdaystaffing.job_changes.get_by_id`](#workdaystaffingjob_changesget_by_id)
  * [`workdaystaffing.job_changes.get_comment_by_id`](#workdaystaffingjob_changesget_comment_by_id)
  * [`workdaystaffing.job_changes.get_comment_info`](#workdaystaffingjob_changesget_comment_info)
  * [`workdaystaffing.job_changes.get_contract_options`](#workdaystaffingjob_changesget_contract_options)
  * [`workdaystaffing.job_changes.get_contract_options_0`](#workdaystaffingjob_changesget_contract_options_0)
  * [`workdaystaffing.job_changes.get_job_classification`](#workdaystaffingjob_changesget_job_classification)
  * [`workdaystaffing.job_changes.get_job_classification_0`](#workdaystaffingjob_changesget_job_classification_0)
  * [`workdaystaffing.job_changes.get_job_profile`](#workdaystaffingjob_changesget_job_profile)
  * [`workdaystaffing.job_changes.get_location_info`](#workdaystaffingjob_changesget_location_info)
  * [`workdaystaffing.job_changes.get_location_info_0`](#workdaystaffingjob_changesget_location_info_0)
  * [`workdaystaffing.job_changes.get_move_team_option`](#workdaystaffingjob_changesget_move_team_option)
  * [`workdaystaffing.job_changes.get_move_team_option_0`](#workdaystaffingjob_changesget_move_team_option_0)
  * [`workdaystaffing.job_changes.get_opening_options`](#workdaystaffingjob_changesget_opening_options)
  * [`workdaystaffing.job_changes.get_opening_options_0`](#workdaystaffingjob_changesget_opening_options_0)
  * [`workdaystaffing.job_changes.get_position_by_id`](#workdaystaffingjob_changesget_position_by_id)
  * [`workdaystaffing.job_changes.get_position_by_subresource_id`](#workdaystaffingjob_changesget_position_by_subresource_id)
  * [`workdaystaffing.job_changes.get_profile`](#workdaystaffingjob_changesget_profile)
  * [`workdaystaffing.job_changes.get_start_details`](#workdaystaffingjob_changesget_start_details)
  * [`workdaystaffing.job_changes.get_start_details_0`](#workdaystaffingjob_changesget_start_details_0)
  * [`workdaystaffing.job_changes.partial_update_location_options`](#workdaystaffingjob_changespartial_update_location_options)
  * [`workdaystaffing.job_changes.partially_update_contract_options`](#workdaystaffingjob_changespartially_update_contract_options)
  * [`workdaystaffing.job_changes.submit_change_job`](#workdaystaffingjob_changessubmit_change_job)
  * [`workdaystaffing.job_changes.update_administrative_options`](#workdaystaffingjob_changesupdate_administrative_options)
  * [`workdaystaffing.job_changes.update_business_title_options`](#workdaystaffingjob_changesupdate_business_title_options)
  * [`workdaystaffing.job_changes.update_comment`](#workdaystaffingjob_changesupdate_comment)
  * [`workdaystaffing.job_changes.update_job_classification_options`](#workdaystaffingjob_changesupdate_job_classification_options)
  * [`workdaystaffing.job_changes.update_job_profile_options`](#workdaystaffingjob_changesupdate_job_profile_options)
  * [`workdaystaffing.job_changes.update_move_team_options`](#workdaystaffingjob_changesupdate_move_team_options)
  * [`workdaystaffing.job_changes.update_opening_options`](#workdaystaffingjob_changesupdate_opening_options)
  * [`workdaystaffing.job_changes.update_position_options`](#workdaystaffingjob_changesupdate_position_options)
  * [`workdaystaffing.job_changes.update_start_details`](#workdaystaffingjob_changesupdate_start_details)
  * [`workdaystaffing.job_families.get_by_id`](#workdaystaffingjob_familiesget_by_id)
  * [`workdaystaffing.job_families.list`](#workdaystaffingjob_familieslist)
  * [`workdaystaffing.job_profiles.get_by_id`](#workdaystaffingjob_profilesget_by_id)
  * [`workdaystaffing.job_profiles.list_collection`](#workdaystaffingjob_profileslist_collection)
  * [`workdaystaffing.jobs.get_collection`](#workdaystaffingjobsget_collection)
  * [`workdaystaffing.jobs.get_job_by_id`](#workdaystaffingjobsget_job_by_id)
  * [`workdaystaffing.jobs.get_workspace`](#workdaystaffingjobsget_workspace)
  * [`workdaystaffing.jobs.get_workspaces`](#workdaystaffingjobsget_workspaces)
  * [`workdaystaffing.organization_assignment_changes.create_change_event`](#workdaystaffingorganization_assignment_changescreate_change_event)
  * [`workdaystaffing.organization_assignment_changes.get_business_unit`](#workdaystaffingorganization_assignment_changesget_business_unit)
  * [`workdaystaffing.organization_assignment_changes.get_business_unit_0`](#workdaystaffingorganization_assignment_changesget_business_unit_0)
  * [`workdaystaffing.organization_assignment_changes.get_comment`](#workdaystaffingorganization_assignment_changesget_comment)
  * [`workdaystaffing.organization_assignment_changes.get_comment_info`](#workdaystaffingorganization_assignment_changesget_comment_info)
  * [`workdaystaffing.organization_assignment_changes.get_company`](#workdaystaffingorganization_assignment_changesget_company)
  * [`workdaystaffing.organization_assignment_changes.get_company_by_id`](#workdaystaffingorganization_assignment_changesget_company_by_id)
  * [`workdaystaffing.organization_assignment_changes.get_cost_center`](#workdaystaffingorganization_assignment_changesget_cost_center)
  * [`workdaystaffing.organization_assignment_changes.get_cost_center_0`](#workdaystaffingorganization_assignment_changesget_cost_center_0)
  * [`workdaystaffing.organization_assignment_changes.get_costing_organizations`](#workdaystaffingorganization_assignment_changesget_costing_organizations)
  * [`workdaystaffing.organization_assignment_changes.get_costing_organizations_0`](#workdaystaffingorganization_assignment_changesget_costing_organizations_0)
  * [`workdaystaffing.organization_assignment_changes.get_custom_organizations`](#workdaystaffingorganization_assignment_changesget_custom_organizations)
  * [`workdaystaffing.organization_assignment_changes.get_custom_organizations_0`](#workdaystaffingorganization_assignment_changesget_custom_organizations_0)
  * [`workdaystaffing.organization_assignment_changes.get_instance`](#workdaystaffingorganization_assignment_changesget_instance)
  * [`workdaystaffing.organization_assignment_changes.get_region`](#workdaystaffingorganization_assignment_changesget_region)
  * [`workdaystaffing.organization_assignment_changes.get_region_by_id`](#workdaystaffingorganization_assignment_changesget_region_by_id)
  * [`workdaystaffing.organization_assignment_changes.get_start_details`](#workdaystaffingorganization_assignment_changesget_start_details)
  * [`workdaystaffing.organization_assignment_changes.get_start_details_0`](#workdaystaffingorganization_assignment_changesget_start_details_0)
  * [`workdaystaffing.organization_assignment_changes.partially_update_company`](#workdaystaffingorganization_assignment_changespartially_update_company)
  * [`workdaystaffing.organization_assignment_changes.partially_update_costing_options`](#workdaystaffingorganization_assignment_changespartially_update_costing_options)
  * [`workdaystaffing.organization_assignment_changes.partially_update_start_details`](#workdaystaffingorganization_assignment_changespartially_update_start_details)
  * [`workdaystaffing.organization_assignment_changes.submit_change_request`](#workdaystaffingorganization_assignment_changessubmit_change_request)
  * [`workdaystaffing.organization_assignment_changes.update_business_unit`](#workdaystaffingorganization_assignment_changesupdate_business_unit)
  * [`workdaystaffing.organization_assignment_changes.update_comment`](#workdaystaffingorganization_assignment_changesupdate_comment)
  * [`workdaystaffing.organization_assignment_changes.update_cost_center`](#workdaystaffingorganization_assignment_changesupdate_cost_center)
  * [`workdaystaffing.organization_assignment_changes.update_custom_organizations`](#workdaystaffingorganization_assignment_changesupdate_custom_organizations)
  * [`workdaystaffing.organization_assignment_changes.update_region`](#workdaystaffingorganization_assignment_changesupdate_region)
  * [`workdaystaffing.supervisory_organizations.get_by_id`](#workdaystaffingsupervisory_organizationsget_by_id)
  * [`workdaystaffing.supervisory_organizations.get_instance`](#workdaystaffingsupervisory_organizationsget_instance)
  * [`workdaystaffing.supervisory_organizations.get_member`](#workdaystaffingsupervisory_organizationsget_member)
  * [`workdaystaffing.supervisory_organizations.get_members`](#workdaystaffingsupervisory_organizationsget_members)
  * [`workdaystaffing.supervisory_organizations.get_org_chart`](#workdaystaffingsupervisory_organizationsget_org_chart)
  * [`workdaystaffing.supervisory_organizations.get_org_chart_0`](#workdaystaffingsupervisory_organizationsget_org_chart_0)
  * [`workdaystaffing.workers.create_check_in`](#workdaystaffingworkerscreate_check_in)
  * [`workdaystaffing.workers.create_check_in_topic`](#workdaystaffingworkerscreate_check_in_topic)
  * [`workdaystaffing.workers.create_external_skill_levels`](#workdaystaffingworkerscreate_external_skill_levels)
  * [`workdaystaffing.workers.create_home_contact_change_process`](#workdaystaffingworkerscreate_home_contact_change_process)
  * [`workdaystaffing.workers.create_skill_item`](#workdaystaffingworkerscreate_skill_item)
  * [`workdaystaffing.workers.create_work_contact_information_changes`](#workdaystaffingworkerscreate_work_contact_information_changes)
  * [`workdaystaffing.workers.delete_check_in`](#workdaystaffingworkersdelete_check_in)
  * [`workdaystaffing.workers.delete_check_in_topic`](#workdaystaffingworkersdelete_check_in_topic)
  * [`workdaystaffing.workers.get_check_in`](#workdaystaffingworkersget_check_in)
  * [`workdaystaffing.workers.get_check_in_topic`](#workdaystaffingworkersget_check_in_topic)
  * [`workdaystaffing.workers.get_check_in_topics`](#workdaystaffingworkersget_check_in_topics)
  * [`workdaystaffing.workers.get_check_ins`](#workdaystaffingworkersget_check_ins)
  * [`workdaystaffing.workers.get_collection_staffing`](#workdaystaffingworkersget_collection_staffing)
  * [`workdaystaffing.workers.get_explicit_skills`](#workdaystaffingworkersget_explicit_skills)
  * [`workdaystaffing.workers.get_explicit_skills_for_skill_enabled`](#workdaystaffingworkersget_explicit_skills_for_skill_enabled)
  * [`workdaystaffing.workers.get_external_skill_level`](#workdaystaffingworkersget_external_skill_level)
  * [`workdaystaffing.workers.get_external_skill_levels`](#workdaystaffingworkersget_external_skill_levels)
  * [`workdaystaffing.workers.get_home_contact_change`](#workdaystaffingworkersget_home_contact_change)
  * [`workdaystaffing.workers.get_service_date`](#workdaystaffingworkersget_service_date)
  * [`workdaystaffing.workers.get_service_dates`](#workdaystaffingworkersget_service_dates)
  * [`workdaystaffing.workers.get_skill_items`](#workdaystaffingworkersget_skill_items)
  * [`workdaystaffing.workers.get_skill_items_by_id`](#workdaystaffingworkersget_skill_items_by_id)
  * [`workdaystaffing.workers.get_staffing_information`](#workdaystaffingworkersget_staffing_information)
  * [`workdaystaffing.workers.get_work_contact_change`](#workdaystaffingworkersget_work_contact_change)
  * [`workdaystaffing.workers.initiate_job_change`](#workdaystaffingworkersinitiate_job_change)
  * [`workdaystaffing.workers.initiate_organization_assignment_change`](#workdaystaffingworkersinitiate_organization_assignment_change)
  * [`workdaystaffing.workers.partially_update_check_in`](#workdaystaffingworkerspartially_update_check_in)
  * [`workdaystaffing.workers.partially_update_check_in_topic`](#workdaystaffingworkerspartially_update_check_in_topic)
  * [`workdaystaffing.workers.save_user_skills`](#workdaystaffingworkerssave_user_skills)
  * [`workdaystaffing.workers.update_check_in`](#workdaystaffingworkersupdate_check_in)
  * [`workdaystaffing.workers.update_check_in_topic_state`](#workdaystaffingworkersupdate_check_in_topic_state)
  * [`workdaystaffing.workers.update_external_skill_level`](#workdaystaffingworkersupdate_external_skill_level)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Workday&serviceName=Staffing&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from workday_staffing_python_sdk import WorkdayStaffing, ApiException

workdaystaffing = WorkdayStaffing(
)

try:
    available_locations_response = workdaystaffing.prompt_values.available_locations(
        effective_date="1970-01-01",
        job="string_example",
        limit=1,
        location="string_example",
        offset=1,
        proposed_manager=[
        "string_example"
    ],
        staffing_event="string_example",
        worker="string_example",
    )
    print(available_locations_response)
except ApiException as e:
    print("Exception when calling PromptValuesApi.available_locations: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from workday_staffing_python_sdk import WorkdayStaffing, ApiException

workdaystaffing = WorkdayStaffing(
)

async def main():
    try:
        available_locations_response = await workdaystaffing.prompt_values.aavailable_locations(
            effective_date="1970-01-01",
            job="string_example",
            limit=1,
            location="string_example",
            offset=1,
            proposed_manager=[
        "string_example"
    ],
            staffing_event="string_example",
            worker="string_example",
        )
        print(available_locations_response)
    except ApiException as e:
        print("Exception when calling PromptValuesApi.available_locations: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from workday_staffing_python_sdk import WorkdayStaffing, ApiException

workdaystaffing = WorkdayStaffing(
)

try:
    available_locations_response = workdaystaffing.prompt_values.raw.available_locations(
        effective_date="1970-01-01",
        job="string_example",
        limit=1,
        location="string_example",
        offset=1,
        proposed_manager=[
        "string_example"
    ],
        staffing_event="string_example",
        worker="string_example",
    )
    pprint(available_locations_response.body)
    pprint(available_locations_response.body["total"])
    pprint(available_locations_response.body["data"])
    pprint(available_locations_response.headers)
    pprint(available_locations_response.status)
    pprint(available_locations_response.round_trip_time)
except ApiException as e:
    print("Exception when calling PromptValuesApi.available_locations: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `workdaystaffing.prompt_values.available_locations`<a id="workdaystaffingprompt_valuesavailable_locations"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
available_locations_response = workdaystaffing.prompt_values.available_locations(
    effective_date="1970-01-01",
    job="string_example",
    limit=1,
    location="string_example",
    offset=1,
    proposed_manager=[
        "string_example"
    ],
    staffing_event="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### job: `str`<a id="job-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### location: `str`<a id="location-str"></a>

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### proposed_manager: List[`str`]<a id="proposed_manager-liststr"></a>

##### staffing_event: `str`<a id="staffing_event-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/jobChangesGroup/locations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_assignment_change_group_cost_centers`<a id="workdaystaffingprompt_valuesget_assignment_change_group_cost_centers"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_assignment_change_group_cost_centers_response = workdaystaffing.prompt_values.get_assignment_change_group_cost_centers(
    effective_date="1970-01-01",
    event="string_example",
    limit=1,
    offset=1,
    organization_type="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### event: `str`<a id="event-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### organization_type: `str`<a id="organization_type-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/organizationAssignmentChangesGroup/costCenters` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_assignment_types`<a id="workdaystaffingprompt_valuesget_assignment_types"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_assignment_types_response = workdaystaffing.prompt_values.get_assignment_types(
    effective_date="1970-01-01",
    job="string_example",
    limit=1,
    location="string_example",
    offset=1,
    proposed_manager=[
        "string_example"
    ],
    staffing_event="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### job: `str`<a id="job-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### location: `str`<a id="location-str"></a>

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### proposed_manager: List[`str`]<a id="proposed_manager-liststr"></a>

##### staffing_event: `str`<a id="staffing_event-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/jobChangesGroup/assignmentTypes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_company_insider_types`<a id="workdaystaffingprompt_valuesget_company_insider_types"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_insider_types_response = workdaystaffing.prompt_values.get_company_insider_types(
    effective_date="1970-01-01",
    job="string_example",
    limit=1,
    location="string_example",
    offset=1,
    proposed_manager=[
        "string_example"
    ],
    staffing_event="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### job: `str`<a id="job-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### location: `str`<a id="location-str"></a>

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### proposed_manager: List[`str`]<a id="proposed_manager-liststr"></a>

##### staffing_event: `str`<a id="staffing_event-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/jobChangesGroup/companyInsiderTypes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_contingent_worker_types`<a id="workdaystaffingprompt_valuesget_contingent_worker_types"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_contingent_worker_types_response = workdaystaffing.prompt_values.get_contingent_worker_types(
    effective_date="1970-01-01",
    job="string_example",
    limit=1,
    location="string_example",
    offset=1,
    proposed_manager=[
        "string_example"
    ],
    staffing_event="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### job: `str`<a id="job-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### location: `str`<a id="location-str"></a>

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### proposed_manager: List[`str`]<a id="proposed_manager-liststr"></a>

##### staffing_event: `str`<a id="staffing_event-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/jobChangesGroup/contingentWorkerTypes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_currency_instances`<a id="workdaystaffingprompt_valuesget_currency_instances"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_currency_instances_response = workdaystaffing.prompt_values.get_currency_instances(
    effective_date="1970-01-01",
    job="string_example",
    limit=1,
    location="string_example",
    offset=1,
    proposed_manager=[
        "string_example"
    ],
    staffing_event="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### job: `str`<a id="job-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### location: `str`<a id="location-str"></a>

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### proposed_manager: List[`str`]<a id="proposed_manager-liststr"></a>

##### staffing_event: `str`<a id="staffing_event-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/jobChangesGroup/currencies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_employee_types`<a id="workdaystaffingprompt_valuesget_employee_types"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_employee_types_response = workdaystaffing.prompt_values.get_employee_types(
    effective_date="1970-01-01",
    job="string_example",
    limit=1,
    location="string_example",
    offset=1,
    proposed_manager=[
        "string_example"
    ],
    staffing_event="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### job: `str`<a id="job-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### location: `str`<a id="location-str"></a>

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### proposed_manager: List[`str`]<a id="proposed_manager-liststr"></a>

##### staffing_event: `str`<a id="staffing_event-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/jobChangesGroup/employeeTypes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_gift_instances`<a id="workdaystaffingprompt_valuesget_gift_instances"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_gift_instances_response = workdaystaffing.prompt_values.get_gift_instances(
    effective_date="1970-01-01",
    event="string_example",
    limit=1,
    offset=1,
    organization_type="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### event: `str`<a id="event-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### organization_type: `str`<a id="organization_type-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/organizationAssignmentChangesGroup/gifts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_grants`<a id="workdaystaffingprompt_valuesget_grants"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_grants_response = workdaystaffing.prompt_values.get_grants(
    effective_date="1970-01-01",
    event="string_example",
    limit=1,
    offset=1,
    organization_type="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### event: `str`<a id="event-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### organization_type: `str`<a id="organization_type-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/organizationAssignmentChangesGroup/grants` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_instances`<a id="workdaystaffingprompt_valuesget_instances"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_response = workdaystaffing.prompt_values.get_instances(
    effective_date="1970-01-01",
    event="string_example",
    limit=1,
    offset=1,
    organization_type="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### event: `str`<a id="event-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### organization_type: `str`<a id="organization_type-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/organizationAssignmentChangesGroup/regions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_instances_0`<a id="workdaystaffingprompt_valuesget_instances_0"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_0_response = workdaystaffing.prompt_values.get_instances_0(
    effective_date="1970-01-01",
    job="string_example",
    limit=1,
    location="string_example",
    offset=1,
    proposed_manager=[
        "string_example"
    ],
    staffing_event="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### job: `str`<a id="job-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### location: `str`<a id="location-str"></a>

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### proposed_manager: List[`str`]<a id="proposed_manager-liststr"></a>

##### staffing_event: `str`<a id="staffing_event-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/jobChangesGroup/reason` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_instances_1`<a id="workdaystaffingprompt_valuesget_instances_1"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_1_response = workdaystaffing.prompt_values.get_instances_1(
    effective_date="1970-01-01",
    event="string_example",
    limit=1,
    offset=1,
    organization_type="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### event: `str`<a id="event-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### organization_type: `str`<a id="organization_type-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/organizationAssignmentChangesGroup/customs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_instances_10`<a id="workdaystaffingprompt_valuesget_instances_10"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_10_response = workdaystaffing.prompt_values.get_instances_10(
    effective_date="1970-01-01",
    job="string_example",
    limit=1,
    location="string_example",
    offset=1,
    proposed_manager=[
        "string_example"
    ],
    staffing_event="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### job: `str`<a id="job-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### location: `str`<a id="location-str"></a>

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### proposed_manager: List[`str`]<a id="proposed_manager-liststr"></a>

##### staffing_event: `str`<a id="staffing_event-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/jobChangesGroup/templates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_instances_11`<a id="workdaystaffingprompt_valuesget_instances_11"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_11_response = workdaystaffing.prompt_values.get_instances_11(
    effective_date="1970-01-01",
    job="string_example",
    limit=1,
    location="string_example",
    offset=1,
    proposed_manager=[
        "string_example"
    ],
    staffing_event="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### job: `str`<a id="job-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### location: `str`<a id="location-str"></a>

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### proposed_manager: List[`str`]<a id="proposed_manager-liststr"></a>

##### staffing_event: `str`<a id="staffing_event-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/jobChangesGroup/workers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_instances_12`<a id="workdaystaffingprompt_valuesget_instances_12"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_12_response = workdaystaffing.prompt_values.get_instances_12(
    effective_date="1970-01-01",
    job="string_example",
    limit=1,
    location="string_example",
    offset=1,
    proposed_manager=[
        "string_example"
    ],
    staffing_event="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### job: `str`<a id="job-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### location: `str`<a id="location-str"></a>

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### proposed_manager: List[`str`]<a id="proposed_manager-liststr"></a>

##### staffing_event: `str`<a id="staffing_event-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/jobChangesGroup/jobs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_instances_13`<a id="workdaystaffingprompt_valuesget_instances_13"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_13_response = workdaystaffing.prompt_values.get_instances_13(
    effective_date="1970-01-01",
    event="string_example",
    limit=1,
    offset=1,
    organization_type="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### event: `str`<a id="event-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### organization_type: `str`<a id="organization_type-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/organizationAssignmentChangesGroup/workers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_instances_14`<a id="workdaystaffingprompt_valuesget_instances_14"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_14_response = workdaystaffing.prompt_values.get_instances_14(
    effective_date="1970-01-01",
    job="string_example",
    limit=1,
    location="string_example",
    offset=1,
    proposed_manager=[
        "string_example"
    ],
    staffing_event="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### job: `str`<a id="job-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### location: `str`<a id="location-str"></a>

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### proposed_manager: List[`str`]<a id="proposed_manager-liststr"></a>

##### staffing_event: `str`<a id="staffing_event-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/jobChangesGroup/workStudyAwards` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_instances_15`<a id="workdaystaffingprompt_valuesget_instances_15"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_15_response = workdaystaffing.prompt_values.get_instances_15(
    effective_date="1970-01-01",
    event="string_example",
    limit=1,
    offset=1,
    organization_type="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### event: `str`<a id="event-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### organization_type: `str`<a id="organization_type-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/organizationAssignmentChangesGroup/positions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_instances_16`<a id="workdaystaffingprompt_valuesget_instances_16"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_16_response = workdaystaffing.prompt_values.get_instances_16(
    effective_date="1970-01-01",
    job="string_example",
    limit=1,
    location="string_example",
    offset=1,
    proposed_manager=[
        "string_example"
    ],
    staffing_event="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### job: `str`<a id="job-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### location: `str`<a id="location-str"></a>

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### proposed_manager: List[`str`]<a id="proposed_manager-liststr"></a>

##### staffing_event: `str`<a id="staffing_event-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/jobChangesGroup/jobRequisitions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_instances_17`<a id="workdaystaffingprompt_valuesget_instances_17"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_17_response = workdaystaffing.prompt_values.get_instances_17(
    effective_date="1970-01-01",
    job="string_example",
    limit=1,
    location="string_example",
    offset=1,
    proposed_manager=[
        "string_example"
    ],
    staffing_event="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### job: `str`<a id="job-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### location: `str`<a id="location-str"></a>

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### proposed_manager: List[`str`]<a id="proposed_manager-liststr"></a>

##### staffing_event: `str`<a id="staffing_event-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/jobChangesGroup/jobProfiles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_instances_18`<a id="workdaystaffingprompt_valuesget_instances_18"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_18_response = workdaystaffing.prompt_values.get_instances_18(
    effective_date="1970-01-01",
    event="string_example",
    limit=1,
    offset=1,
    organization_type="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### event: `str`<a id="event-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### organization_type: `str`<a id="organization_type-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/organizationAssignmentChangesGroup/companies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_instances_19`<a id="workdaystaffingprompt_valuesget_instances_19"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_19_response = workdaystaffing.prompt_values.get_instances_19(
    effective_date="1970-01-01",
    job="string_example",
    limit=1,
    location="string_example",
    offset=1,
    proposed_manager=[
        "string_example"
    ],
    staffing_event="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### job: `str`<a id="job-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### location: `str`<a id="location-str"></a>

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### proposed_manager: List[`str`]<a id="proposed_manager-liststr"></a>

##### staffing_event: `str`<a id="staffing_event-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/jobChangesGroup/jobClassifications` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_instances_2`<a id="workdaystaffingprompt_valuesget_instances_2"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_2_response = workdaystaffing.prompt_values.get_instances_2(
    effective_date="1970-01-01",
    event="string_example",
    limit=1,
    offset=1,
    organization_type="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### event: `str`<a id="event-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### organization_type: `str`<a id="organization_type-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/organizationAssignmentChangesGroup/programs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_instances_3`<a id="workdaystaffingprompt_valuesget_instances_3"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_3_response = workdaystaffing.prompt_values.get_instances_3(
    effective_date="1970-01-01",
    event="string_example",
    limit=1,
    offset=1,
    organization_type="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### event: `str`<a id="event-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### organization_type: `str`<a id="organization_type-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/organizationAssignmentChangesGroup/jobs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_instances_4`<a id="workdaystaffingprompt_valuesget_instances_4"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_4_response = workdaystaffing.prompt_values.get_instances_4(
    effective_date="1970-01-01",
    event="string_example",
    limit=1,
    offset=1,
    organization_type="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### event: `str`<a id="event-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### organization_type: `str`<a id="organization_type-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/organizationAssignmentChangesGroup/funds` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_instances_5`<a id="workdaystaffingprompt_valuesget_instances_5"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_5_response = workdaystaffing.prompt_values.get_instances_5(
    effective_date="1970-01-01",
    job="string_example",
    limit=1,
    location="string_example",
    offset=1,
    proposed_manager=[
        "string_example"
    ],
    staffing_event="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### job: `str`<a id="job-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### location: `str`<a id="location-str"></a>

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### proposed_manager: List[`str`]<a id="proposed_manager-liststr"></a>

##### staffing_event: `str`<a id="staffing_event-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/jobChangesGroup/workersCompensationCodeOverrides` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_instances_6`<a id="workdaystaffingprompt_valuesget_instances_6"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_6_response = workdaystaffing.prompt_values.get_instances_6(
    effective_date="1970-01-01",
    job="string_example",
    limit=1,
    location="string_example",
    offset=1,
    proposed_manager=[
        "string_example"
    ],
    staffing_event="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### job: `str`<a id="job-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### location: `str`<a id="location-str"></a>

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### proposed_manager: List[`str`]<a id="proposed_manager-liststr"></a>

##### staffing_event: `str`<a id="staffing_event-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/jobChangesGroup/workShifts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_instances_7`<a id="workdaystaffingprompt_valuesget_instances_7"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_7_response = workdaystaffing.prompt_values.get_instances_7(
    effective_date="1970-01-01",
    event="string_example",
    limit=1,
    offset=1,
    organization_type="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### event: `str`<a id="event-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### organization_type: `str`<a id="organization_type-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/organizationAssignmentChangesGroup/businessUnits` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_instances_8`<a id="workdaystaffingprompt_valuesget_instances_8"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_8_response = workdaystaffing.prompt_values.get_instances_8(
    effective_date="1970-01-01",
    job="string_example",
    limit=1,
    location="string_example",
    offset=1,
    proposed_manager=[
        "string_example"
    ],
    staffing_event="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### job: `str`<a id="job-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### location: `str`<a id="location-str"></a>

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### proposed_manager: List[`str`]<a id="proposed_manager-liststr"></a>

##### staffing_event: `str`<a id="staffing_event-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/jobChangesGroup/frequencies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_instances_9`<a id="workdaystaffingprompt_valuesget_instances_9"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_9_response = workdaystaffing.prompt_values.get_instances_9(
    effective_date="1970-01-01",
    job="string_example",
    limit=1,
    location="string_example",
    offset=1,
    proposed_manager=[
        "string_example"
    ],
    staffing_event="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### job: `str`<a id="job-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### location: `str`<a id="location-str"></a>

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### proposed_manager: List[`str`]<a id="proposed_manager-liststr"></a>

##### staffing_event: `str`<a id="staffing_event-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/jobChangesGroup/payRateTypes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_options`<a id="workdaystaffingprompt_valuesget_options"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_options_response = workdaystaffing.prompt_values.get_options(
    effective_date="1970-01-01",
    job="string_example",
    limit=1,
    location="string_example",
    offset=1,
    proposed_manager=[
        "string_example"
    ],
    staffing_event="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### job: `str`<a id="job-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### location: `str`<a id="location-str"></a>

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### proposed_manager: List[`str`]<a id="proposed_manager-liststr"></a>

##### staffing_event: `str`<a id="staffing_event-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/jobChangesGroup/headcountOptions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_proposed_positions`<a id="workdaystaffingprompt_valuesget_proposed_positions"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_proposed_positions_response = workdaystaffing.prompt_values.get_proposed_positions(
    effective_date="1970-01-01",
    job="string_example",
    limit=1,
    location="string_example",
    offset=1,
    proposed_manager=[
        "string_example"
    ],
    staffing_event="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### job: `str`<a id="job-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### location: `str`<a id="location-str"></a>

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### proposed_manager: List[`str`]<a id="proposed_manager-liststr"></a>

##### staffing_event: `str`<a id="staffing_event-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/jobChangesGroup/proposedPosition` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_supervisory_org_values`<a id="workdaystaffingprompt_valuesget_supervisory_org_values"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_supervisory_org_values_response = workdaystaffing.prompt_values.get_supervisory_org_values(
    effective_date="1970-01-01",
    job="string_example",
    limit=1,
    location="string_example",
    offset=1,
    proposed_manager=[
        "string_example"
    ],
    staffing_event="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### job: `str`<a id="job-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### location: `str`<a id="location-str"></a>

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### proposed_manager: List[`str`]<a id="proposed_manager-liststr"></a>

##### staffing_event: `str`<a id="staffing_event-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/jobChangesGroup/supervisoryOrganization` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_time_types`<a id="workdaystaffingprompt_valuesget_time_types"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_time_types_response = workdaystaffing.prompt_values.get_time_types(
    effective_date="1970-01-01",
    job="string_example",
    limit=1,
    location="string_example",
    offset=1,
    proposed_manager=[
        "string_example"
    ],
    staffing_event="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### job: `str`<a id="job-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### location: `str`<a id="location-str"></a>

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### proposed_manager: List[`str`]<a id="proposed_manager-liststr"></a>

##### staffing_event: `str`<a id="staffing_event-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/jobChangesGroup/timeTypes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_worker_types`<a id="workdaystaffingprompt_valuesget_worker_types"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_worker_types_response = workdaystaffing.prompt_values.get_worker_types(
    effective_date="1970-01-01",
    job="string_example",
    limit=1,
    location="string_example",
    offset=1,
    proposed_manager=[
        "string_example"
    ],
    staffing_event="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### job: `str`<a id="job-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### location: `str`<a id="location-str"></a>

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### proposed_manager: List[`str`]<a id="proposed_manager-liststr"></a>

##### staffing_event: `str`<a id="staffing_event-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/jobChangesGroup/workerTypes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.prompt_values.get_workspace_instances`<a id="workdaystaffingprompt_valuesget_workspace_instances"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_workspace_instances_response = workdaystaffing.prompt_values.get_workspace_instances(
    effective_date="1970-01-01",
    job="string_example",
    limit=1,
    location="string_example",
    offset=1,
    proposed_manager=[
        "string_example"
    ],
    staffing_event="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

##### job: `str`<a id="job-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### location: `str`<a id="location-str"></a>

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### proposed_manager: List[`str`]<a id="proposed_manager-liststr"></a>

##### staffing_event: `str`<a id="staffing_event-str"></a>

##### worker: `str`<a id="worker-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_staffing_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/jobChangesGroup/workSpaces` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.get_admin_options`<a id="workdaystaffingjob_changesget_admin_options"></a>

Retrieves the administrative options for the specified job change ID.

The {subResourceID} path parameter must be the same as the {ID} value.

Note that there are no localization constraints in this API version. This method returns the workingFTE and paidFTE fields even if the fields have not been localized.

Secured by: Staffing Actions: Administrator

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_admin_options_response = workdaystaffing.job_changes.get_admin_options(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`ChangeJobAdministrativeDetailsDataF8f20079bc5a1000089ccb7f6a8800ea`](./workday_staffing_python_sdk/pydantic/change_job_administrative_details_data_f8f20079bc5a1000089ccb7f6a8800ea.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/administrative/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.get_administrative_options`<a id="workdaystaffingjob_changesget_administrative_options"></a>

Retrieves the administrative options for the specified job change ID.

The {subResourceID} path parameter must be the same as the {ID} value.

Note that there are no localization constraints in this API version. This method returns the workingFTE and paidFTE fields even if the fields have not been localized.

Secured by: Staffing Actions: Administrator

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_administrative_options_response = workdaystaffing.job_changes.get_administrative_options(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`JobChangesGetAdministrativeOptionsResponse`](./workday_staffing_python_sdk/pydantic/job_changes_get_administrative_options_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/administrative` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.get_business_title`<a id="workdaystaffingjob_changesget_business_title"></a>

Retrieves a business title for the specified specified job change ID.
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Actions: Business Title

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_business_title_response = workdaystaffing.job_changes.get_business_title(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`ChangeJobBusinessTitle3db8095ffa18100013a5f96969ca0102`](./workday_staffing_python_sdk/pydantic/change_job_business_title3db8095ffa18100013a5f96969ca0102.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/businessTitle/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.get_business_title_0`<a id="workdaystaffingjob_changesget_business_title_0"></a>

Retrieves a business title for the specified specified job change ID.
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Actions: Business Title

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_business_title_0_response = workdaystaffing.job_changes.get_business_title_0(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`JobChangesGetBusinessTitleResponse`](./workday_staffing_python_sdk/pydantic/job_changes_get_business_title_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/businessTitle` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.get_by_id`<a id="workdaystaffingjob_changesget_by_id"></a>

Retrieves a change job event with the specified ID.

Secured by: Change Job (Mass Action), Change Job (REST Service), Staffing Actions, Staffing Actions: Academic Pay, Staffing Actions: Additional Job Classifications, Staffing Actions: Administrator, Staffing Actions: Attachments, Staffing Actions: Business Title, Staffing Actions: Change Job Date and Reason, Staffing Actions: Compensation for All Job Profiles, Staffing Actions: Contract Details, Staffing Actions: Hire Student, Staffing Actions: Job Profile, Staffing Actions: View \~Worker\~ Start Date Correction

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = workdaystaffing.job_changes.get_by_id(
    id="ID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

#### 🔄 Return<a id="🔄-return"></a>

[`ChangeJobDefaultRepresentation6cc31ee444d010000bb4153a954300e7`](./workday_staffing_python_sdk/pydantic/change_job_default_representation6cc31ee444d010000bb4153a954300e7.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.get_comment_by_id`<a id="workdaystaffingjob_changesget_comment_by_id"></a>

Returns the comment information for the specified job change ID.
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Change Job (Mass Action), Change Job (REST Service)

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_comment_by_id_response = workdaystaffing.job_changes.get_comment_by_id(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`JobChangesGetCommentByIdResponse`](./workday_staffing_python_sdk/pydantic/job_changes_get_comment_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/comment` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.get_comment_info`<a id="workdaystaffingjob_changesget_comment_info"></a>

Returns the comment information for the specified job change ID.
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Change Job (Mass Action), Change Job (REST Service)

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_comment_info_response = workdaystaffing.job_changes.get_comment_info(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`Comments7d98fd55aeee100022968e52a1b31c60`](./workday_staffing_python_sdk/pydantic/comments7d98fd55aeee100022968e52a1b31c60.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/comment/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.get_contract_options`<a id="workdaystaffingjob_changesget_contract_options"></a>

Returns the contract options for the specified job change ID.

The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Actions: Contract Details

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_contract_options_response = workdaystaffing.job_changes.get_contract_options(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`JobChangesGetContractOptionsResponse`](./workday_staffing_python_sdk/pydantic/job_changes_get_contract_options_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/contract` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.get_contract_options_0`<a id="workdaystaffingjob_changesget_contract_options_0"></a>

Returns the contract options for the specified job change ID.

The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Actions: Contract Details

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_contract_options_0_response = workdaystaffing.job_changes.get_contract_options_0(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`ChangeJobContractDetailsData27ec818d10d010000386ce823ac20107`](./workday_staffing_python_sdk/pydantic/change_job_contract_details_data27ec818d10d010000386ce823ac20107.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/contract/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.get_job_classification`<a id="workdaystaffingjob_changesget_job_classification"></a>

Retrieves a job classification for the specified job change ID.

The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Actions: Additional Job Classifications

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_job_classification_response = workdaystaffing.job_changes.get_job_classification(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`JobChangesGetJobClassificationResponse`](./workday_staffing_python_sdk/pydantic/job_changes_get_job_classification_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/jobClassification` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.get_job_classification_0`<a id="workdaystaffingjob_changesget_job_classification_0"></a>

Retrieves a job classification for the specified job change ID.

The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Actions: Additional Job Classifications

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_job_classification_0_response = workdaystaffing.job_changes.get_job_classification_0(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`ChangeJobJobClassificationData354103f196361000084489bcb281017f`](./workday_staffing_python_sdk/pydantic/change_job_job_classification_data354103f196361000084489bcb281017f.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/jobClassification/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.get_job_profile`<a id="workdaystaffingjob_changesget_job_profile"></a>

Retrieves a job profile for the specified job change ID.
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Actions: Job Profile

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_job_profile_response = workdaystaffing.job_changes.get_job_profile(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`JobChangesGetJobProfileResponse`](./workday_staffing_python_sdk/pydantic/job_changes_get_job_profile_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/jobProfile` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.get_location_info`<a id="workdaystaffingjob_changesget_location_info"></a>

Returns the location information for the specified job change ID.
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Actions: Location

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_location_info_response = workdaystaffing.job_changes.get_location_info(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`JobChangesGetLocationInfoResponse`](./workday_staffing_python_sdk/pydantic/job_changes_get_location_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/location` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.get_location_info_0`<a id="workdaystaffingjob_changesget_location_info_0"></a>

Returns the location information for the specified job change ID.
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Actions: Location

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_location_info_0_response = workdaystaffing.job_changes.get_location_info_0(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`ChangeJobLocation90151d6c4ff110001b4a46091678025c`](./workday_staffing_python_sdk/pydantic/change_job_location90151d6c4ff110001b4a46091678025c.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/location/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.get_move_team_option`<a id="workdaystaffingjob_changesget_move_team_option"></a>

Retrieves a move team option from the specified job change ID.

The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Actions: Move Manager's Team

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_move_team_option_response = workdaystaffing.job_changes.get_move_team_option(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`ChangeJobMoveTeamData544fdf5c01da1000238ad82d26d90146`](./workday_staffing_python_sdk/pydantic/change_job_move_team_data544fdf5c01da1000238ad82d26d90146.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/moveTeam/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.get_move_team_option_0`<a id="workdaystaffingjob_changesget_move_team_option_0"></a>

Retrieves a move team option from the specified job change ID.

The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Actions: Move Manager's Team

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_move_team_option_0_response = workdaystaffing.job_changes.get_move_team_option_0(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`JobChangesGetMoveTeamOptionResponse`](./workday_staffing_python_sdk/pydantic/job_changes_get_move_team_option_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/moveTeam` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.get_opening_options`<a id="workdaystaffingjob_changesget_opening_options"></a>

Retrieves the opening options for the specified job change ID.
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Actions: Change Job Date and Reason

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_opening_options_response = workdaystaffing.job_changes.get_opening_options(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`JobChangesGetOpeningOptionsResponse`](./workday_staffing_python_sdk/pydantic/job_changes_get_opening_options_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/opening` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.get_opening_options_0`<a id="workdaystaffingjob_changesget_opening_options_0"></a>

Retrieves the opening options for the specified job change ID.
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Actions: Change Job Date and Reason

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_opening_options_0_response = workdaystaffing.job_changes.get_opening_options_0(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`ChangeJobOpeningData97af9049a5fd10001c4888d654170000`](./workday_staffing_python_sdk/pydantic/change_job_opening_data97af9049a5fd10001c4888d654170000.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/opening/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.get_position_by_id`<a id="workdaystaffingjob_changesget_position_by_id"></a>

Retrieves a position for the specified job change ID.

The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Actions: Select or Create Position

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_position_by_id_response = workdaystaffing.job_changes.get_position_by_id(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`JobChangesGetPositionByIdResponse`](./workday_staffing_python_sdk/pydantic/job_changes_get_position_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/position` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.get_position_by_subresource_id`<a id="workdaystaffingjob_changesget_position_by_subresource_id"></a>

Retrieves a position for the specified job change ID.

The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Actions: Select or Create Position

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_position_by_subresource_id_response = workdaystaffing.job_changes.get_position_by_subresource_id(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`ChangeJobPositionDataDfc4e58f7308100018bd1c459f435221`](./workday_staffing_python_sdk/pydantic/change_job_position_data_dfc4e58f7308100018bd1c459f435221.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/position/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.get_profile`<a id="workdaystaffingjob_changesget_profile"></a>

Retrieves a job profile for the specified job change ID.
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Actions: Job Profile

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_profile_response = workdaystaffing.job_changes.get_profile(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`ChangeJobJobProfileData3db8095ffa18100013f019a27a1f0115`](./workday_staffing_python_sdk/pydantic/change_job_job_profile_data3db8095ffa18100013f019a27a1f0115.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/jobProfile/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.get_start_details`<a id="workdaystaffingjob_changesget_start_details"></a>

Retrieves the start details for the specified job change ID.

Secured by: Staffing Actions: Change Job Date and Reason

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_start_details_response = workdaystaffing.job_changes.get_start_details(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`JobChangesStartDetailsDataCe861a6a360d10002d40f176b7180020`](./workday_staffing_python_sdk/pydantic/job_changes_start_details_data_ce861a6a360d10002d40f176b7180020.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/startDetails/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.get_start_details_0`<a id="workdaystaffingjob_changesget_start_details_0"></a>

Retrieves the start details for the specified job change ID.

Secured by: Staffing Actions: Change Job Date and Reason

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_start_details_0_response = workdaystaffing.job_changes.get_start_details_0(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`JobChangesGetStartDetailsResponse`](./workday_staffing_python_sdk/pydantic/job_changes_get_start_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/startDetails` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.partial_update_location_options`<a id="workdaystaffingjob_changespartial_update_location_options"></a>

Partially updates the location options for the specified job change ID. 
The {subResourceID} path parameter must be the same as the {ID} value.

You can call GET /jobChanges/{ID}/location/{subResourceID} to get the existing data to update. 

The same Workday UI validations apply with this PATCH method. The data updates in this PATCH method do not persist until you call POST /jobChanges/{ID}/submit.

In the request body, specify at least this request field: location{id}. 

To retrieve a location ID, you can call the GET /values/jobChangesGroup/locations prompt endpoint, which takes the job change ID as the staffingEvent query parameter. It returns HREF links to locations by location categories for the staffingEvent. You can filter the results by effectiveDate. By default, it returns locations on the current date. 

To retrieve a workShift ID, call the GET /values/jobChangesGroup/workShifts prompt endpoint with the location query parameter. It returns work shifts by location. If you don't specify the location parameter, it returns an empty result.

To retrieve a workSpace ID, call the GET /values/jobChangesGroup/workSpaces prompt endpoint with the location query parameter. It returns HREF links to workspaces by configured prompt categories for the specified location. You can filter the results by effectiveDate. By default, it returns workspaces on the current date.

Secured by: Staffing Actions: Location

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
partial_update_location_options_response = workdaystaffing.job_changes.partial_update_location_options(
    body={
        "scheduled_hours": 40,
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    location=None,
    scheduled_hours=40,
    work_shift=None,
    work_space=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### location: `Location90151d6c4ff110001bfa027116820278`<a id="location-location90151d6c4ff110001bfa027116820278"></a>

##### scheduled_hours: `int`<a id="scheduled_hours-int"></a>

The new scheduled hours for the worker as of the effective date.

##### work_shift: `WorkShift0ee7bb8b41db1000143d4e4822174f2e`<a id="work_shift-workshift0ee7bb8b41db1000143d4e4822174f2e"></a>

##### work_space: `WorkSpace0ee7bb8b41db10001e7db6a6c3e55663`<a id="work_space-workspace0ee7bb8b41db10001e7db6a6c3e55663"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ChangeJobLocation90151d6c4ff110001b4a46091678025c`](./workday_staffing_python_sdk/type/change_job_location90151d6c4ff110001b4a46091678025c.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ChangeJobLocation90151d6c4ff110001b4a46091678025c`](./workday_staffing_python_sdk/pydantic/change_job_location90151d6c4ff110001b4a46091678025c.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/location/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.partially_update_contract_options`<a id="workdaystaffingjob_changespartially_update_contract_options"></a>

Partially updates the contract details options for the specified job change ID.
The {subResourceID} path parameter must be the same as the {ID} value.

You can call GET /jobChanges/{ID}/contract/{subResourceID} to get the existing data to update. 

The same Workday UI validations apply with this PATCH method. The updates in this PATCH method do not persist until you call POST /jobChanges/{ID}/submit.


To retrieve a frequency ID, call the GET /values/jobChangesGroup/frequencies prompt endpoint, which takes the job change ID as the staffingEvent query parameter. It returns all frequencies based on staffing event for contingent workers. By default, it returns all frequencies in the tenant.

To retrieve a currency ID, call the GET /values/jobChangesGroup/currencies prompt endpoint, which takes the job change ID as the staffingEvent query parameter. If you specify the staffingEvent parameter, it returns HREF links to active currencies by prompt category. By default, it returns all active currencies.

Secured by: Staffing Actions: Contract Details

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
partially_update_contract_options_response = workdaystaffing.job_changes.partially_update_contract_options(
    body={
        "assignment_details": "Sample Contract Assignment Details",
        "contract_end_date": "2021-01-01T01:00:00.000Z",
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    assignment_details="Sample Contract Assignment Details",
    contract_end_date="2021-01-01T01:00:00.000Z",
    contract_pay_rate={},
    currency=None,
    frequency=None,
    purchase_order=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### assignment_details: `str`<a id="assignment_details-str"></a>

The new contract assignment details for the contingent worker as of the effective date.

##### contract_end_date: `date`<a id="contract_end_date-date"></a>

The contract end date for the position as of this business process.

##### contract_pay_rate: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="contract_pay_rate-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

The new contract pay rate for the contingent worker as of the effective date.

##### currency: `Currency2d0ca2cb2448100009c54386a8570e07`<a id="currency-currency2d0ca2cb2448100009c54386a8570e07"></a>

##### frequency: `Frequency2d0ca2cb2448100009c5436d5d670e06`<a id="frequency-frequency2d0ca2cb2448100009c5436d5d670e06"></a>

##### purchase_order: `PurchaseOrder2d0ca2cb2448100009c5433bcff60e05`<a id="purchase_order-purchaseorder2d0ca2cb2448100009c5433bcff60e05"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ChangeJobContractDetailsData27ec818d10d010000386ce823ac20107`](./workday_staffing_python_sdk/type/change_job_contract_details_data27ec818d10d010000386ce823ac20107.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ChangeJobContractDetailsData27ec818d10d010000386ce823ac20107`](./workday_staffing_python_sdk/pydantic/change_job_contract_details_data27ec818d10d010000386ce823ac20107.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/contract/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.submit_change_job`<a id="workdaystaffingjob_changessubmit_change_job"></a>

Submits the specified change job ID. 

To submit the Change Job event and initiate the Change Job business process, specify an empty request body: {}.
To save for later, specify this request body:
{
    "businessProcessParameters": {
        "action":{
            "id": "d9e41a8c446c11de98360015c5e6daf6"
        }
    }
}

The action id value is the Workday ID of the "Save for Later" action. If you submit this endpoint with the Save for Later action, you can no longer edit nor resubmit the Change Job event using the REST APIs. The user with correct permissions can edit and submit the saved Change Job event in the Workday UI.

Secured by: Change Job (Mass Action), Change Job (REST Service)

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
submit_change_job_response = workdaystaffing.job_changes.submit_change_job(
    body={
        "validation": "Sample Validation",
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    business_process_parameters=None,
    status=None,
    validation="Sample Validation",
    id="string_example",
    descriptor="Lorem ipsum dolor sit ame",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### business_process_parameters: `BusinessProcessParameters5afc0b4b5a4610002aaebb8180cd2261`<a id="business_process_parameters-businessprocessparameters5afc0b4b5a4610002aaebb8180cd2261"></a>

##### status: `Status54e611eca2c910000fbc4599be0b0112`<a id="status-status54e611eca2c910000fbc4599be0b0112"></a>

##### validation: `str`<a id="validation-str"></a>

Validation message for an action event triggered by a condition.

##### id: `str`<a id="id-str"></a>

Id of the instance

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EventState54e611eca2c910000fbc4579181c0111`](./workday_staffing_python_sdk/type/event_state54e611eca2c910000fbc4579181c0111.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EventState54e611eca2c910000fbc4579181c0111`](./workday_staffing_python_sdk/pydantic/event_state54e611eca2c910000fbc4579181c0111.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/submit` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.update_administrative_options`<a id="workdaystaffingjob_changesupdate_administrative_options"></a>

Partially updates the administrative options for the specified job change ID.
The {subResourceID} path parameter must be the same as the {ID} value.

You can call GET /jobChanges/{ID}/administrative/{subResourceID} to get the existing data to update. 

The same Workday UI validations apply with this PATCH method. The updates in this PATCH method do not persist until you call POST /jobChanges/{ID}/submit.

Note that there are no localization constraints in this API version. You can update the workingFTE and paidFTE fields even if the fields have not been localized.

To retrieve a positionWorkerType ID, you can call the GET /values/jobChangesGroup/employeeTypes prompt endpoint, with staffingEvent and location query parameters. If you specify the staffingEvent parameter, it returns HREF links to employee types by country. By default, it returns all employee types, excluding contingent workers.

For the positionWorkerType ID, you can also call the GET /values/jobChangesGroup/contingentWorkerTypes prompt endpoint, with staffingEvent and location query parameters. If you specify the staffingEvent parameter, it returns HREF links to contingent worker types for staffing event. If you specify location, it returns HREF links to contingent worker types by location or country. By default, it returns all contingent worker types.

To retrieve a workersCompensationCodeOverride ID, call the GET /values/jobChangesGroup/workersCompensationCodeOverrides prompt endpoint, which takes the job change ID as the staffing Event query parameter. 

To retrieve a payRateType ID, call the GET /values/jobChangesGroup/payRateTypes prompt endpoint, which takes the job change ID as the staffingEvent query parameter. It returns all pay rate types based on staffing event for contingent workers. By default, it returns all pay rate types in the tenant. 

To retrieve companyInsiderType IDs, call the GET /values/jobChangesGroup/companyInsiderTypes prompt endpoint, which returns all company insider types in the tenant. 

To retrieve an assignmentType ID, call the GET /values/jobChangesGroup/assignmentTypes prompt endpoint, which takes the job change ID as the staffingEvent query parameter. If you specify the staffingEvent parameter, it returns assignmentTypes for the staffingEvent. By default, it returns all active assignment types.

To retrieve a workStudy ID, call the GET /values/jobChangesGroup/workStudyAwards prompt endpoint, which takes the job change ID as the staffingEvent query parameter. If you specify the staffingEvent parameter, it returns work study awards for the staffingEvent. By default, it returns all work studies in the tenant.

To retrieve a timeType ID, call the GET /values/jobChangesGroup/timeTypes prompt endpoint, which takes the job change ID as the staffingEvent query parameter. If you specify the staffingEvent parameter, it returns time types for the staffingEvent. By default, it returns all time types based on the Relax Hiring Restrictions tenant configuration.

Secured by: Staffing Actions: Administrator

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_administrative_options_response = workdaystaffing.job_changes.update_administrative_options(
    body={
        "fte": 40,
        "notify_by": "2020-01-17T17:00:00.000Z",
        "first_day_of_work": "2020-01-20T16:00:00.000Z",
        "default_weekly_hours": 40,
        "working_fte": 40,
        "specify_working_fte": True,
        "specify_paid_fte": True,
        "paid_fte": 40,
        "end_employment_date": "2024-03-23T07:00:00.000Z",
        "expected_assignment_end_date": "2024-03-23T07:00:00.000Z",
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    pay_rate_type=None,
    workers_compensation_code_override=None,
    fte=40,
    notify_by="2020-01-17T17:00:00.000Z",
    company_insider_types=[
        {
            "descriptor": "Lorem ipsum dolor sit ame",
        }
    ],
    first_day_of_work="2020-01-20T16:00:00.000Z",
    default_weekly_hours=40,
    position_worker_type=None,
    working_fte=40,
    specify_working_fte=True,
    time_type=None,
    specify_paid_fte=True,
    paid_fte=40,
    work_study=None,
    assignment_type=None,
    end_employment_date="2024-03-23T07:00:00.000Z",
    expected_assignment_end_date="2024-03-23T07:00:00.000Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### pay_rate_type: `PayRateTypeD25283821c01100016756a14eb650000`<a id="pay_rate_type-payratetyped25283821c01100016756a14eb650000"></a>

##### workers_compensation_code_override: `WorkersCompensationCodeOverride05d4c45042b61000138500e185e0013f`<a id="workers_compensation_code_override-workerscompensationcodeoverride05d4c45042b61000138500e185e0013f"></a>

##### fte: `int`<a id="fte-int"></a>

Full Time Equivalent for a worker calculated by scheduled weekly hours divided by default weekly hours either current or proposed.

##### notify_by: `date`<a id="notify_by-date"></a>

Returns the date that the employee should be notified for a termination.

##### company_insider_types: List[`ChangeJobCompanyInsiderTypesData05d4c45042b61000131e4b2132f30137`]<a id="company_insider_types-listchangejobcompanyinsidertypesdata05d4c45042b61000131e4b2132f30137"></a>

The new company insider types for the worker as of the effective date.

##### first_day_of_work: `date`<a id="first_day_of_work-date"></a>

The first day of work for the worker, as specified on the Hire, Add International Assignment, or Add Job transaction. This field will not return a value for any other transaction.

##### default_weekly_hours: `int`<a id="default_weekly_hours-int"></a>

The new default weekly hours for the worker as of the effective date.

##### position_worker_type: `PositionWorkerType05d4c45042b610001030ee47f2c90118`<a id="position_worker_type-positionworkertype05d4c45042b610001030ee47f2c90118"></a>

##### working_fte: `int`<a id="working_fte-int"></a>

The working full time equivalent for the worker as of the effective date.

##### specify_working_fte: `bool`<a id="specify_working_fte-bool"></a>

True if working full time equivalent is specified on a worker as of the effective date.

##### time_type: `TimeType05d4c45042b610000bb540b7458e0108`<a id="time_type-timetype05d4c45042b610000bb540b7458e0108"></a>

##### specify_paid_fte: `bool`<a id="specify_paid_fte-bool"></a>

True if paid full time equivalent is specified on a worker as of the effective date.

##### paid_fte: `int`<a id="paid_fte-int"></a>

The paid full time equivalent for the worker as of the effective date.

##### work_study: `WorkStudy05d4c45042b610000ba2f83c70f30101`<a id="work_study-workstudy05d4c45042b610000ba2f83c70f30101"></a>

##### assignment_type: `AssignmentType23929e1f68ca10000d6940d6bde56963`<a id="assignment_type-assignmenttype23929e1f68ca10000d6940d6bde56963"></a>

##### end_employment_date: `date`<a id="end_employment_date-date"></a>

The new End Employment Date for the worker. If the worker has an Employee Contract sub event, this field will return that end date instead.

##### expected_assignment_end_date: `date`<a id="expected_assignment_end_date-date"></a>

For a past or current business process, the value of the Expected Assignment End Date field that is being (or was) proposed in the process.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ChangeJobAdministrativeDetailsDataF8f20079bc5a1000089ccb7f6a8800ea`](./workday_staffing_python_sdk/type/change_job_administrative_details_data_f8f20079bc5a1000089ccb7f6a8800ea.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ChangeJobAdministrativeDetailsDataF8f20079bc5a1000089ccb7f6a8800ea`](./workday_staffing_python_sdk/pydantic/change_job_administrative_details_data_f8f20079bc5a1000089ccb7f6a8800ea.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/administrative/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.update_business_title_options`<a id="workdaystaffingjob_changesupdate_business_title_options"></a>

Partially updates the businessTitle options for the specified change job ID.

The {subResourceID} path parameter must be the same as the {ID} value.

You can call GET /jobChanges/{ID}/businessTitle/{subResourceID} to get the existing data to update. 

The same Workday UI validations apply with this PATCH method. The updates in this PATCH method do not persist until you call POST /jobChanges/{ID}/submit.

Secured by: Staffing Actions: Business Title

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_business_title_options_response = workdaystaffing.job_changes.update_business_title_options(
    body={
        "business_title": "Sample Business Title",
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    business_title="Sample Business Title",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### business_title: `str`<a id="business_title-str"></a>

The new business title for the worker as of the effective date.  If there is no business title override, this field defaults to the job title or job profile name.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ChangeJobBusinessTitle3db8095ffa18100013a5f96969ca0102`](./workday_staffing_python_sdk/type/change_job_business_title3db8095ffa18100013a5f96969ca0102.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ChangeJobBusinessTitle3db8095ffa18100013a5f96969ca0102`](./workday_staffing_python_sdk/pydantic/change_job_business_title3db8095ffa18100013a5f96969ca0102.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/businessTitle/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.update_comment`<a id="workdaystaffingjob_changesupdate_comment"></a>

Updates the comment for the specified change job ID.
The {subResourceID} path parameter must be the same as the {ID} value.

The data updates in this PATCH method do not persist until you call POST /jobChanges/{ID}/submit.

You can call GET /jobChanges/{ID}/comment/{subResourceID} to get the existing data to update.

Secured by: Change Job (Mass Action), Change Job (REST Service)

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_comment_response = workdaystaffing.job_changes.update_comment(
    body={
        "comment": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    comment="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### comment: `str`<a id="comment-str"></a>

The business process comment for a worker event before it's submitted.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Comments7d98fd55aeee100022968e52a1b31c60`](./workday_staffing_python_sdk/type/comments7d98fd55aeee100022968e52a1b31c60.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Comments7d98fd55aeee100022968e52a1b31c60`](./workday_staffing_python_sdk/pydantic/comments7d98fd55aeee100022968e52a1b31c60.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/comment/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.update_job_classification_options`<a id="workdaystaffingjob_changesupdate_job_classification_options"></a>

Partially updates the job classifications for the specified job change ID. 
The {subResourceID} path parameter must be the same as the {ID} value.

You can call GET /jobChanges/{ID}/jobClassification/{subResourceID} to get the existing data to update. 

The same Workday UI validations apply with this PATCH method. The updates in this PATCH method do not persist until you call POST /jobChanges/{ID}/submit.

In the request body, specify at least this required field: additionalJobClassifications[ {id} ]. 

To retrieve an additionalJobClassifications ID, call the GET /values/jobChangesGroup/jobClassifications prompt endpoint with the location and/or staffingEvent query parameter. It returns HREF links to job classifications by location for the staffing event. It returns an empty result if both location and staffingEvent are not specified. You can filter the results by effectiveDate. By default, it returns job classifications on the current date.

Secured by: Staffing Actions: Additional Job Classifications

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_job_classification_options_response = workdaystaffing.job_changes.update_job_classification_options(
    body={
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    additional_job_classifications=[
        {
            "descriptor": "Lorem ipsum dolor sit ame",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### additional_job_classifications: List[`ChangeJobAdditionalJobClassificationData27ec818d10d0100003600115b5200102`]<a id="additional_job_classifications-listchangejobadditionaljobclassificationdata27ec818d10d0100003600115b5200102"></a>

Additional Job Classifications Proposed By Staffing Event

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ChangeJobJobClassificationData354103f196361000084489bcb281017f`](./workday_staffing_python_sdk/type/change_job_job_classification_data354103f196361000084489bcb281017f.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ChangeJobJobClassificationData354103f196361000084489bcb281017f`](./workday_staffing_python_sdk/pydantic/change_job_job_classification_data354103f196361000084489bcb281017f.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/jobClassification/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.update_job_profile_options`<a id="workdaystaffingjob_changesupdate_job_profile_options"></a>

Partially updates the job profile options for the specified job change ID.

The {subResourceID} path parameter must be the same as the {ID} value.

You can call GET /jobChanges/{ID}/jobProfile/{subResourceID} to get the existing data to update.

The same Workday UI validations apply with this PATCH method. The updates in this PATCH method do not persist until you call POST /jobChanges/{ID}/submit.

In the request body, specify at least this required field: jobProfile{id}

To retrieve a jobProfile ID, call the GET /values/jobChangesGroup/jobProfiles prompt endpoint, which takes the job change ID as the staffingEvent query parameter. If you specify the staffingEvent parameter, it returns HREF links to the job profiles by the prompt category. If you don't specify the staffingEvent parameter, it returns all job profiles, regardless of their categories. You can also filter the job profiles by the effectiveDate query parameter. The default is the current date.

Secured by: Staffing Actions: Job Profile

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_job_profile_options_response = workdaystaffing.job_changes.update_job_profile_options(
    body={
        "job_title": "Sample Job Title",
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    job_profile=None,
    job_title="Sample Job Title",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### job_profile: `JobProfile3db8095ffa18100013f019afc6d30116`<a id="job_profile-jobprofile3db8095ffa18100013f019afc6d30116"></a>

##### job_title: `str`<a id="job_title-str"></a>

The new job title for the worker as of the effective date.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ChangeJobJobProfileData3db8095ffa18100013f019a27a1f0115`](./workday_staffing_python_sdk/type/change_job_job_profile_data3db8095ffa18100013f019a27a1f0115.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ChangeJobJobProfileData3db8095ffa18100013f019a27a1f0115`](./workday_staffing_python_sdk/pydantic/change_job_job_profile_data3db8095ffa18100013f019a27a1f0115.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/jobProfile/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.update_move_team_options`<a id="workdaystaffingjob_changesupdate_move_team_options"></a>

Partially updates the moveTeam options for the specified change job ID.

The {subResourceID} path parameter must be the same as the {ID} value.

You can call GET /jobChanges/{ID}/moveTeam/{subResourceID} to get the existing data to update. 

The same Workday UI validations apply with this PATCH method. The updates in this PATCH method do not persist until you call POST /jobChanges/{ID}/submit.

Secured by: Staffing Actions: Move Manager's Team

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_move_team_options_response = workdaystaffing.job_changes.update_move_team_options(
    body={
        "move_team": True,
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    move_team=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### move_team: `bool`<a id="move_team-bool"></a>

Returns a boolean that indicates whether teams reporting to the Manager moved with them during the Change Job Event.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ChangeJobMoveTeamData544fdf5c01da1000238ad82d26d90146`](./workday_staffing_python_sdk/type/change_job_move_team_data544fdf5c01da1000238ad82d26d90146.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ChangeJobMoveTeamData544fdf5c01da1000238ad82d26d90146`](./workday_staffing_python_sdk/pydantic/change_job_move_team_data544fdf5c01da1000238ad82d26d90146.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/moveTeam/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.update_opening_options`<a id="workdaystaffingjob_changesupdate_opening_options"></a>

Partially updates the opening options for the specified job change ID. 
The {subResourceID} path parameter must be the same as the {ID} value.

You can call GET /jobChanges/{ID}/opening/{subResourceID} to get the existing data to update. 

The same Workday UI validations apply with this PATCH method. The updates in this PATCH method do not persist until you call POST /jobChanges/{ID}/submit.

In the request body, specify at least this required field: headcountOption{id} 

To retrieve a headcountOption ID, call the GET /values/jobChangesGroup/headcountOptions prompt endpoint, which takes the job change ID as the staffingEvent query parameter. By default, it returns all headcount options.

Secured by: Staffing Actions: Change Job Date and Reason

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_opening_options_response = workdaystaffing.job_changes.update_opening_options(
    body={
        "opening_available_for_overlap": True,
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    headcount_option=None,
    opening_available_for_overlap=True,
    id="string_example",
    descriptor="Lorem ipsum dolor sit ame",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### headcount_option: `HeadcountOption97af9049a5fd10001c48896fbde30000`<a id="headcount_option-headcountoption97af9049a5fd10001c48896fbde30000"></a>

##### opening_available_for_overlap: `bool`<a id="opening_available_for_overlap-bool"></a>

Returns true if the value for 'Available for job overlap' box is checked

##### id: `str`<a id="id-str"></a>

Id of the instance

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ChangeJobOpeningData97af9049a5fd10001c4888d654170000`](./workday_staffing_python_sdk/type/change_job_opening_data97af9049a5fd10001c4888d654170000.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ChangeJobOpeningData97af9049a5fd10001c4888d654170000`](./workday_staffing_python_sdk/pydantic/change_job_opening_data97af9049a5fd10001c4888d654170000.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/opening/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.update_position_options`<a id="workdaystaffingjob_changesupdate_position_options"></a>

Partially updates the position options for the specified job change ID.
The {subResourceID} path parameter must be the same as the {ID} value.

You can call GET /jobChanges/{ID}/startDetails/{subResourceID} to get the existing data to update. 

The same Workday UI validations apply with this PATCH method. The updates in this PATCH method do not persist until you call POST /jobChanges/{ID}/submit.

In the request body, specify at least these request fields: position{id}, createPosition, closePosition, availableForOverlap

To retrieve a position ID, call the GET /values/jobChangesGroup/proposedPosition prompt endpoint, which takes the job change ID as the staffingEvent query parameter. It returns HREF links to proposed positions based on staffing event for contingent workers. You can filter the results by effectiveDate. By default, it returns all proposed positions on current date.

Secured by: Staffing Actions: Select or Create Position

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_position_options_response = workdaystaffing.job_changes.update_position_options(
    body={
        "create_position": True,
        "available_for_overlap": True,
        "close_position": True,
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    create_position=True,
    available_for_overlap=True,
    position=None,
    close_position=True,
    job_requisition=None,
    id="string_example",
    descriptor="Lorem ipsum dolor sit ame",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### create_position: `bool`<a id="create_position-bool"></a>

Returns true if the position is being created.

##### available_for_overlap: `bool`<a id="available_for_overlap-bool"></a>

Returns true if the value for 'Available for job overlap' box is checked

##### position: `PositionDfc4e58f730810001ad60369c23452d1`<a id="position-positiondfc4e58f730810001ad60369c23452d1"></a>

##### close_position: `bool`<a id="close_position-bool"></a>

Returns true if the position is being closed.

##### job_requisition: `JobRequisitionDfc4e58f730810001ad60325d9bc52cf`<a id="job_requisition-jobrequisitiondfc4e58f730810001ad60325d9bc52cf"></a>

##### id: `str`<a id="id-str"></a>

Id of the instance

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ChangeJobPositionDataDfc4e58f7308100018bd1c459f435221`](./workday_staffing_python_sdk/type/change_job_position_data_dfc4e58f7308100018bd1c459f435221.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ChangeJobPositionDataDfc4e58f7308100018bd1c459f435221`](./workday_staffing_python_sdk/pydantic/change_job_position_data_dfc4e58f7308100018bd1c459f435221.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/position/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_changes.update_start_details`<a id="workdaystaffingjob_changesupdate_start_details"></a>

Partially updates the start details for the specified job change ID. 
The {subResourceID} path parameter must be the same as the {ID} value.

You can call GET /jobChanges/{ID}/startDetails/{subResourceID} to get the existing data to update. 

The same Workday UI validations apply with this PATCH method. The updates in this PATCH method do not persist until you call POST /jobChanges/{ID}/submit.

In the request body, specify at least these request fields: date, reason{id}. 

To retrieve a reason ID, call the GET /values/jobChangesGroup/reason prompt endpoint, which takes the job change ID as the staffingEvent query parameter. If you specify the staffingEvent parameter, it returns change job reasons for the staffingEvent, by the change job category. By default, it returns all change job categories and reasons.

Secured by: Staffing Actions: Change Job Date and Reason

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_start_details_response = workdaystaffing.job_changes.update_start_details(
    body={
        "use_next_pay_period": True,
        "date": "2020-01-18T01:00:00.000Z",
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    worker=None,
    use_next_pay_period=True,
    template=None,
    job=None,
    date="2020-01-18T01:00:00.000Z",
    location=None,
    reason=None,
    supervisory_organization=None,
    id="string_example",
    descriptor="Lorem ipsum dolor sit ame",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### worker: `Worker271bbd673582100010110b9f9a6d99e1`<a id="worker-worker271bbd673582100010110b9f9a6d99e1"></a>

##### use_next_pay_period: `bool`<a id="use_next_pay_period-bool"></a>

Next Pay Period?

##### template: `Template2b1b95dfe4af100009f30dc769a31686`<a id="template-template2b1b95dfe4af100009f30dc769a31686"></a>

##### job: `Job35b8f199c29410002508ffd7ad6101f3`<a id="job-job35b8f199c29410002508ffd7ad6101f3"></a>

##### date: `date`<a id="date-date"></a>

The date this business process takes effect.

##### location: `Location6da81665c26510001fc6b1d42fae5f7b`<a id="location-location6da81665c26510001fc6b1d42fae5f7b"></a>

##### reason: `Reason6da81665c26510001f34d0a154765e9b`<a id="reason-reason6da81665c26510001f34d0a154765e9b"></a>

##### supervisory_organization: `SupervisoryOrganizationE3267ea37e6f100032c00c34a99e74d8`<a id="supervisory_organization-supervisoryorganizatione3267ea37e6f100032c00c34a99e74d8"></a>

##### id: `str`<a id="id-str"></a>

Id of the instance

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JobChangesStartDetailsDataCe861a6a360d10002d40f176b7180020`](./workday_staffing_python_sdk/type/job_changes_start_details_data_ce861a6a360d10002d40f176b7180020.py)
#### 🔄 Return<a id="🔄-return"></a>

[`JobChangesStartDetailsDataCe861a6a360d10002d40f176b7180020`](./workday_staffing_python_sdk/pydantic/job_changes_start_details_data_ce861a6a360d10002d40f176b7180020.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobChanges/{ID}/startDetails/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_families.get_by_id`<a id="workdaystaffingjob_familiesget_by_id"></a>

Retrieves a job family with the specified ID.

Secured by: Job Information

Scope: Jobs & Positions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = workdaystaffing.job_families.get_by_id(
    id="ID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

#### 🔄 Return<a id="🔄-return"></a>

[`JobFamilyView51ed1475e9e6100005d10fcedc5a000a`](./workday_staffing_python_sdk/pydantic/job_family_view51ed1475e9e6100005d10fcedc5a000a.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobFamilies/{ID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_families.list`<a id="workdaystaffingjob_familieslist"></a>

Retrieves a collection of job families.

Secured by: Job Information

Scope: Jobs & Positions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = workdaystaffing.job_families.list(
    inactive=True,
    job_family_group=[
        "string_example"
    ],
    job_profile=[
        "string_example"
    ],
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### inactive: `bool`<a id="inactive-bool"></a>

If true, the method returns inactive job families. Default is false.

##### job_family_group: List[`str`]<a id="job_family_group-liststr"></a>

The job family group for the job family. You can specify more than 1 jobFamilyGroup query parameter.

##### job_profile: List[`str`]<a id="job_profile-liststr"></a>

The job profile for the job family. You can specify more than 1 jobFamilyGroup query parameter. For possible values, you can use a returned id from GET /jobProfiles.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`JobFamiliesListResponse`](./workday_staffing_python_sdk/pydantic/job_families_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobFamilies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_profiles.get_by_id`<a id="workdaystaffingjob_profilesget_by_id"></a>

Retrieves a job profile with the specified ID.

Secured by: Job Profile: View, Public Job: View

Scope: Jobs & Positions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = workdaystaffing.job_profiles.get_by_id(
    id="ID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

#### 🔄 Return<a id="🔄-return"></a>

[`JobProfileDetailView7deab99f645f10000bd5e61a1b780041`](./workday_staffing_python_sdk/pydantic/job_profile_detail_view7deab99f645f10000bd5e61a1b780041.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobProfiles/{ID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.job_profiles.list_collection`<a id="workdaystaffingjob_profileslist_collection"></a>

Retrieves a collection of job profiles.

Secured by: Job Profile: View, Public Job: View

Scope: Jobs & Positions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_collection_response = workdaystaffing.job_profiles.list_collection(
    include_inactive=True,
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### include_inactive: `bool`<a id="include_inactive-bool"></a>

If true, the method returns inactive job profiles. Default is false.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`JobProfilesListCollectionResponse`](./workday_staffing_python_sdk/pydantic/job_profiles_list_collection_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobProfiles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.jobs.get_collection`<a id="workdaystaffingjobsget_collection"></a>

Retrieves a collection of jobs.

Secured by: Worker Position: View

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_collection_response = workdaystaffing.jobs.get_collection(
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`JobsGetCollectionResponse`](./workday_staffing_python_sdk/pydantic/jobs_get_collection_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.jobs.get_job_by_id`<a id="workdaystaffingjobsget_job_by_id"></a>

Retrieves a job with the specified job ID.

Secured by: Worker Position: View

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_job_by_id_response = workdaystaffing.jobs.get_job_by_id(
    id="ID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

#### 🔄 Return<a id="🔄-return"></a>

[`JobData1bfa8925c50510000ae4479925510026`](./workday_staffing_python_sdk/pydantic/job_data1bfa8925c50510000ae4479925510026.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobs/{ID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.jobs.get_workspace`<a id="workdaystaffingjobsget_workspace"></a>

Retrieves a single workspace for the specified job ID.

Secured by: Worker Data: Public Worker Reports

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_workspace_response = workdaystaffing.jobs.get_workspace(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`JobWorkspaceData1005157e3d631000144205466a6c13d3`](./workday_staffing_python_sdk/pydantic/job_workspace_data1005157e3d631000144205466a6c13d3.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobs/{ID}/workspace/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.jobs.get_workspaces`<a id="workdaystaffingjobsget_workspaces"></a>

Retrieves a collection of workspaces for the specified job ID.

Secured by: Worker Data: Public Worker Reports

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_workspaces_response = workdaystaffing.jobs.get_workspaces(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`JobsGetWorkspacesResponse`](./workday_staffing_python_sdk/pydantic/jobs_get_workspaces_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobs/{ID}/workspace` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.create_change_event`<a id="workdaystaffingorganization_assignment_changescreate_change_event"></a>

Creates a new change organization assignment event for a specific filled or unfilled position, which returns a new change organization assignment ID. Specify the new ID in subsequent requests that update or get information about the change organization assignment event.

In the request body, specify at least this required field: date, job {id}."

Secured by: Change Organization Assignment (REST)

Scope: Organizations and Roles

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_change_event_response = workdaystaffing.organization_assignment_changes.create_change_event(
    body={
        "position": None,
        "date": "2024-03-23T07:00:00.000Z",
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    position=None,
    mass_action_worksheet=None,
    mass_action_header=None,
    date="2024-03-23T07:00:00.000Z",
    id="string_example",
    descriptor="Lorem ipsum dolor sit ame",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### position: `PositionCf97466f96d9100029bffcf91c120001`<a id="position-positioncf97466f96d9100029bffcf91c120001"></a>

##### mass_action_worksheet: `MassActionWorksheet31485c9a93c0100007276cf4e5640000`<a id="mass_action_worksheet-massactionworksheet31485c9a93c0100007276cf4e5640000"></a>

##### mass_action_header: `MassActionHeaderCf97466f96d910002bd32afbf0000001`<a id="mass_action_header-massactionheadercf97466f96d910002bd32afbf0000001"></a>

##### date: `date`<a id="date-date"></a>

The effective date of the business process event using the yyyy-mm-dd format.

##### id: `str`<a id="id-str"></a>

Id of the instance

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrganizationAssignmentChangesPostPositionCf97466f96d9100029bffcf91c120000`](./workday_staffing_python_sdk/type/organization_assignment_changes_post_position_cf97466f96d9100029bffcf91c120000.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationAssignmentChangesPostPositionCf97466f96d9100029bffcf91c120000`](./workday_staffing_python_sdk/pydantic/organization_assignment_changes_post_position_cf97466f96d9100029bffcf91c120000.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.get_business_unit`<a id="workdaystaffingorganization_assignment_changesget_business_unit"></a>

Retrieves a business unit for the specified organization assignment change ID. 
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Organizations: Business Unit

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_business_unit_response = workdaystaffing.organization_assignment_changes.get_business_unit(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationAssignmentChangesBusinessUnitData5aabf8e28cb310002520b2a2b31d0365`](./workday_staffing_python_sdk/pydantic/organization_assignment_changes_business_unit_data5aabf8e28cb310002520b2a2b31d0365.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}/businessUnit/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.get_business_unit_0`<a id="workdaystaffingorganization_assignment_changesget_business_unit_0"></a>

Retrieves a business unit for the specified organization assignment change ID.
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Organizations: Business Unit

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_business_unit_0_response = workdaystaffing.organization_assignment_changes.get_business_unit_0(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationAssignmentChangesGetBusinessUnitResponse`](./workday_staffing_python_sdk/pydantic/organization_assignment_changes_get_business_unit_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}/businessUnit` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.get_comment`<a id="workdaystaffingorganization_assignment_changesget_comment"></a>

Retrieves the comment information for the specified organization assignment change ID.
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Change Organization Assignment (REST), Change Organization Assignments for  \~Worker\~ (Mass Action)

Scope: Organizations and Roles

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_comment_response = workdaystaffing.organization_assignment_changes.get_comment(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationAssignmentChangesGetCommentResponse`](./workday_staffing_python_sdk/pydantic/organization_assignment_changes_get_comment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}/comment` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.get_comment_info`<a id="workdaystaffingorganization_assignment_changesget_comment_info"></a>

Retrieves the comment information for the specified organization assignment change ID.
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Change Organization Assignment (REST), Change Organization Assignments for  \~Worker\~ (Mass Action)

Scope: Organizations and Roles

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_comment_info_response = workdaystaffing.organization_assignment_changes.get_comment_info(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`Comments7d98fd55aeee100022968e52a1b31c60`](./workday_staffing_python_sdk/pydantic/comments7d98fd55aeee100022968e52a1b31c60.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}/comment/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.get_company`<a id="workdaystaffingorganization_assignment_changesget_company"></a>

Retrieves a company for the specified organization assignment change ID.
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Organizations: Company

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_response = workdaystaffing.organization_assignment_changes.get_company(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationAssignmentChangesGetCompanyResponse`](./workday_staffing_python_sdk/pydantic/organization_assignment_changes_get_company_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}/company` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.get_company_by_id`<a id="workdaystaffingorganization_assignment_changesget_company_by_id"></a>

Retrieves a company for the specified organization assignment change ID. 
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Organizations: Company

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_by_id_response = workdaystaffing.organization_assignment_changes.get_company_by_id(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationAssignmentChangesCompanyData652d516fdff41000086e0b9c96950354`](./workday_staffing_python_sdk/pydantic/organization_assignment_changes_company_data652d516fdff41000086e0b9c96950354.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}/company/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.get_cost_center`<a id="workdaystaffingorganization_assignment_changesget_cost_center"></a>

Retrieves a cost center for the specified organization assignment change ID. 
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Organizations: Cost Center

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_cost_center_response = workdaystaffing.organization_assignment_changes.get_cost_center(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationAssignmentChangesCostCenterData5aabf8e28cb3100010a999db2700024e`](./workday_staffing_python_sdk/pydantic/organization_assignment_changes_cost_center_data5aabf8e28cb3100010a999db2700024e.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}/costCenter/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.get_cost_center_0`<a id="workdaystaffingorganization_assignment_changesget_cost_center_0"></a>

Retrieves a cost center for the specified organization assignment change ID.
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Organizations: Cost Center

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_cost_center_0_response = workdaystaffing.organization_assignment_changes.get_cost_center_0(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationAssignmentChangesGetCostCenterResponse`](./workday_staffing_python_sdk/pydantic/organization_assignment_changes_get_cost_center_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}/costCenter` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.get_costing_organizations`<a id="workdaystaffingorganization_assignment_changesget_costing_organizations"></a>

Retrieves the costing organizations for the specified organization assignment change ID. Costing organizations include: Grants, Funds, Programs, and Gifts.
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Organizations: Grant, Fund, Program, Gift

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_costing_organizations_response = workdaystaffing.organization_assignment_changes.get_costing_organizations(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationAssignmentChangesCostingDataA18edb56aca0100014a4a09dc57e045a`](./workday_staffing_python_sdk/pydantic/organization_assignment_changes_costing_data_a18edb56aca0100014a4a09dc57e045a.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}/costing/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.get_costing_organizations_0`<a id="workdaystaffingorganization_assignment_changesget_costing_organizations_0"></a>

Retrieves the costing organizations for the specified organization assignment change ID. Costing organizations include: Grants, Funds, Programs, and Gifts.
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Organizations: Grant, Fund, Program, Gift

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_costing_organizations_0_response = workdaystaffing.organization_assignment_changes.get_costing_organizations_0(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationAssignmentChangesGetCostingOrganizationsResponse`](./workday_staffing_python_sdk/pydantic/organization_assignment_changes_get_costing_organizations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}/costing` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.get_custom_organizations`<a id="workdaystaffingorganization_assignment_changesget_custom_organizations"></a>

Retrieves the custom organizations for the specified organization assignment change ID.
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Organizations: Custom Organization

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_custom_organizations_response = workdaystaffing.organization_assignment_changes.get_custom_organizations(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationAssignmentChangesCustomOrganizationDetailsData53cd2b632146100011e9bf4e7041551f`](./workday_staffing_python_sdk/pydantic/organization_assignment_changes_custom_organization_details_data53cd2b632146100011e9bf4e7041551f.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}/customOrganizations/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.get_custom_organizations_0`<a id="workdaystaffingorganization_assignment_changesget_custom_organizations_0"></a>

Retrieves the custom organizations for the specified organization assignment change ID.
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Organizations: Custom Organization

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_custom_organizations_0_response = workdaystaffing.organization_assignment_changes.get_custom_organizations_0(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationAssignmentChangesGetCustomOrganizationsResponse`](./workday_staffing_python_sdk/pydantic/organization_assignment_changes_get_custom_organizations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}/customOrganizations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.get_instance`<a id="workdaystaffingorganization_assignment_changesget_instance"></a>

Retrieves information about an organization assignment change event with the specified ID.

Secured by: Change Organization Assignment (REST), Staffing Organizations: Business Unit, Staffing Organizations: Company, Staffing Organizations: Cost Center, Staffing Organizations: Custom Organization, Staffing Organizations: Grant, Fund, Program, Gift, Staffing Organizations: Header, Staffing Organizations: Region

Scope: Organizations and Roles, Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instance_response = workdaystaffing.organization_assignment_changes.get_instance(
    id="ID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

#### 🔄 Return<a id="🔄-return"></a>

[`ChangeOrganizationAssignmentDefaultRepresentationDb2f38bfb555100012de1eb17c2f00ff`](./workday_staffing_python_sdk/pydantic/change_organization_assignment_default_representation_db2f38bfb555100012de1eb17c2f00ff.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.get_region`<a id="workdaystaffingorganization_assignment_changesget_region"></a>

Retrieves a region for the specified organization assignment change ID.
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Organizations: Region

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_region_response = workdaystaffing.organization_assignment_changes.get_region(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationAssignmentChangesGetRegionResponse`](./workday_staffing_python_sdk/pydantic/organization_assignment_changes_get_region_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}/region` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.get_region_by_id`<a id="workdaystaffingorganization_assignment_changesget_region_by_id"></a>

Retrieves a region for the specified organization assignment change ID. 
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Organizations: Region

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_region_by_id_response = workdaystaffing.organization_assignment_changes.get_region_by_id(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationAssignmentChangesRegionDataA18edb56aca0100006997e68e5780373`](./workday_staffing_python_sdk/pydantic/organization_assignment_changes_region_data_a18edb56aca0100006997e68e5780373.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}/region/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.get_start_details`<a id="workdaystaffingorganization_assignment_changesget_start_details"></a>

Retrieves the start details for the specified organization assignment change ID.
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Organizations: Header

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_start_details_response = workdaystaffing.organization_assignment_changes.get_start_details(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationAssignmentChangesStartDetailsData90009f2bfc49100017b10cd07d19063b`](./workday_staffing_python_sdk/pydantic/organization_assignment_changes_start_details_data90009f2bfc49100017b10cd07d19063b.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}/startDetails/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.get_start_details_0`<a id="workdaystaffingorganization_assignment_changesget_start_details_0"></a>

Retrieves the start details for the specified organization assignment change ID.
The {subResourceID} path parameter must be the same as the {ID} value.

Secured by: Staffing Organizations: Header

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_start_details_0_response = workdaystaffing.organization_assignment_changes.get_start_details_0(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationAssignmentChangesGetStartDetailsResponse`](./workday_staffing_python_sdk/pydantic/organization_assignment_changes_get_start_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}/startDetails` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.partially_update_company`<a id="workdaystaffingorganization_assignment_changespartially_update_company"></a>

Partially updates the company for the specified organization assignment change ID. 
The {subResourceID} path parameter must be the same as the {ID} value.

You can call GET /organizationAssignmentChanges/{ID}/company/{subResourceID} to get the existing data to update. 

The same Workday UI validations apply with this PATCH method. The data updates in this PATCH method do not persist until you call POST /organizationAssignmentChanges/{ID}/submit.

In the request body, specify the Workday ID of the company. 

To retrieve a companies ID, call the GET /values/organizationAssignmentChangesGroup/companies prompt endpoint, which takes the change organization assignment ID as the event query parameter. If you specify the event parameter, it returns HREF links to the companies by organization, as of the event's effective date. If you don't specify the event parameter, it returns HREF links to the companies by active organization based on the current date.

Secured by: Staffing Organizations: Company

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
partially_update_company_response = workdaystaffing.organization_assignment_changes.partially_update_company(
    body={
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    company=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### company: `Company56fe0dd0eca1100019cfe097d26a03f2`<a id="company-company56fe0dd0eca1100019cfe097d26a03f2"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrganizationAssignmentChangesCompanyData652d516fdff41000086e0b9c96950354`](./workday_staffing_python_sdk/type/organization_assignment_changes_company_data652d516fdff41000086e0b9c96950354.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationAssignmentChangesCompanyData652d516fdff41000086e0b9c96950354`](./workday_staffing_python_sdk/pydantic/organization_assignment_changes_company_data652d516fdff41000086e0b9c96950354.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}/company/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.partially_update_costing_options`<a id="workdaystaffingorganization_assignment_changespartially_update_costing_options"></a>

Partially updates the costing organizations for the specified organization assignment change ID. Costing organizations include: Grants, Funds, Programs, and Gifts.
The {subResourceID} path parameter must be the same as the {ID} value.

You can call GET /organizationAssignmentChanges/{ID}/costing/{subResourceID} to get the existing data to update. 

The same Workday UI validations apply with this PATCH method. The data updates in this PATCH method do not persist until you call POST /organizationAssignmentChanges/{ID}/submit.

In the request body, specify the Workday ID of the grant, program, gift, or fund you want to update.

To retrieve a grants ID, call the GET /values/organizationAssignmentChangesGroup/grants prompt endpoint, which takes the change organization assignment ID as the event query parameter. If you specify the event parameter, it returns HREF links to the grants by organization, as of the event's effective date. If you don't specify the event parameter, it returns HREF links to the grants by active organization based on the current date. 

To retrieve a funds ID, call the GET /values/organizationAssignmentChangesGroup/funds prompt endpoint, which takes the change organization assignment ID as the event query parameter. If you specify the event parameter, it returns HREF links to the funds by organization, as of the event's effective date. If you don't specify the event parameter, it returns HREF links to the funds by active organization based on the current date. 

To retrieve a programs ID, call the GET /values/organizationAssignmentChangesGroup/programs prompt endpoint, which takes the change organization assignment ID as the event query parameter. If you specify the event parameter, it returns HREF links to the programs by organization, as of the event's effective date. If you don't specify the event parameter, it returns HREF links to the programs by active organization based on the current date. 

To retrieve a gifts ID, call the GET /values/organizationAssignmentChangesGroup/gifts prompt endpoint, which takes the change organization assignment ID as the event query parameter. If you specify the event parameter, it returns HREF links to the gifts by organization, as of the event's effective date. If you don't specify the event parameter, it returns HREF links to the gifts by active organization based on the current date.

Secured by: Staffing Organizations: Grant, Fund, Program, Gift

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
partially_update_costing_options_response = workdaystaffing.organization_assignment_changes.partially_update_costing_options(
    body={
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    grant=None,
    program=None,
    gift=None,
    fund=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### grant: `GrantA18edb56aca0100014a4a0bcf25c045e`<a id="grant-granta18edb56aca0100014a4a0bcf25c045e"></a>

##### program: `ProgramA18edb56aca0100014a4a0b7ddf7045d`<a id="program-programa18edb56aca0100014a4a0b7ddf7045d"></a>

##### gift: `GiftA18edb56aca0100014a4a0a9f876045b`<a id="gift-gifta18edb56aca0100014a4a0a9f876045b"></a>

##### fund: `FundA18edb56aca0100014a4a0b27352045c`<a id="fund-funda18edb56aca0100014a4a0b27352045c"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrganizationAssignmentChangesCostingDataA18edb56aca0100014a4a09dc57e045a`](./workday_staffing_python_sdk/type/organization_assignment_changes_costing_data_a18edb56aca0100014a4a09dc57e045a.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationAssignmentChangesCostingDataA18edb56aca0100014a4a09dc57e045a`](./workday_staffing_python_sdk/pydantic/organization_assignment_changes_costing_data_a18edb56aca0100014a4a09dc57e045a.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}/costing/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.partially_update_start_details`<a id="workdaystaffingorganization_assignment_changespartially_update_start_details"></a>

Partially updates the start details for the specified organization assignment change ID. 
The {subResourceID} path parameter must be the same as the {ID} value.

In the request body, specify the effective date for the event. 

You can call GET /organizationAssignmentChanges/{ID}/startDetails/{subResourceID} to get the existing data to update. 

You can only update the date field once the event is initiated. These fields are read-only: worker, supervisoryOrganization, and position.

The same Workday UI validations apply with this PATCH method. 

The updates in this PATCH method do not persist until you call POST /organizationAssignmentChanges/{ID}/submit.

Secured by: Staffing Organizations: Header

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
partially_update_start_details_response = workdaystaffing.organization_assignment_changes.partially_update_start_details(
    body={
        "date": "2024-03-23T07:00:00.000Z",
        "position": None,
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    date="2024-03-23T07:00:00.000Z",
    supervisory_organization=None,
    position=None,
    worker=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### date: `date`<a id="date-date"></a>

The date this business process takes effect.

##### supervisory_organization: `SupervisoryOrganization827372de445710001cfe36968a480000`<a id="supervisory_organization-supervisoryorganization827372de445710001cfe36968a480000"></a>

##### position: `Position827372de4457100019c0e9c5977d0000`<a id="position-position827372de4457100019c0e9c5977d0000"></a>

##### worker: `Worker90009f2bfc4910001b166d44a72c0727`<a id="worker-worker90009f2bfc4910001b166d44a72c0727"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrganizationAssignmentChangesStartDetailsData90009f2bfc49100017b10cd07d19063b`](./workday_staffing_python_sdk/type/organization_assignment_changes_start_details_data90009f2bfc49100017b10cd07d19063b.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationAssignmentChangesStartDetailsData90009f2bfc49100017b10cd07d19063b`](./workday_staffing_python_sdk/pydantic/organization_assignment_changes_start_details_data90009f2bfc49100017b10cd07d19063b.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}/startDetails/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.submit_change_request`<a id="workdaystaffingorganization_assignment_changessubmit_change_request"></a>

Submits the organization assignment change event for the specified ID, and initiates the Change Organization Assignment business process.

Submitting this request with an empty request body { } is equivalent to clicking the Submit button on the Change Organization Assgingment task in Workday.

For the equivalent of clicking the Save For Later button, specify the Save for Later Workday ID, ""d9e41a8c446c11de98360015c5e6daf6"", in the status{id} request field. 

Example:
{ ""status"": {
    ""id"": ""d9e41a8c446c11de98360015c5e6daf6""
  }
}

Secured by: Change Organization Assignment (REST)

Scope: Organizations and Roles

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
submit_change_request_response = workdaystaffing.organization_assignment_changes.submit_change_request(
    body={
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    business_process_parameters=None,
    id="string_example",
    descriptor="Lorem ipsum dolor sit ame",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### business_process_parameters: `BusinessProcessParameters23782ad3f54110002073aab65def00fb`<a id="business_process_parameters-businessprocessparameters23782ad3f54110002073aab65def00fb"></a>

##### id: `str`<a id="id-str"></a>

Id of the instance

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EventStateOrganizationAssignmentF3e1ff305e2d100003327f7b7fa103f1`](./workday_staffing_python_sdk/type/event_state_organization_assignment_f3e1ff305e2d100003327f7b7fa103f1.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EventStateOrganizationAssignmentF3e1ff305e2d100003327f7b7fa103f1`](./workday_staffing_python_sdk/pydantic/event_state_organization_assignment_f3e1ff305e2d100003327f7b7fa103f1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}/submit` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.update_business_unit`<a id="workdaystaffingorganization_assignment_changesupdate_business_unit"></a>

Partially updates the business unit option for the specified change organization assignment ID.
The {subResourceID} path parameter must be the same as the {ID} value.

You can call GET /organizationAssignmentChanges/{ID}/businessUnit/{subResourceID} to get the existing data to update. 

The same Workday UI validations apply with this PATCH method. The data updates in this PATCH method do not persist until you call POST /organizationAssignmentChanges/{ID}/submit.

In the request body, specify the Workday ID of the business unit. 

To retrieve a businessUnit ID, call the GET /values/organizationAssignmentChangesGroup/businessUnit prompt endpoint, which takes the change organization assignment ID as the event query parameter. If you specify the event parameter, it returns HREF links to the business units by organization, as of the event's effective date. If you don't specify the event parameter, it returns HREF links to the business units by active organization based on the current date.

Secured by: Staffing Organizations: Business Unit

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_business_unit_response = workdaystaffing.organization_assignment_changes.update_business_unit(
    body={
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    business_unit=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### business_unit: `BusinessUnit5aabf8e28cb310002520b2aabc470366`<a id="business_unit-businessunit5aabf8e28cb310002520b2aabc470366"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrganizationAssignmentChangesBusinessUnitData5aabf8e28cb310002520b2a2b31d0365`](./workday_staffing_python_sdk/type/organization_assignment_changes_business_unit_data5aabf8e28cb310002520b2a2b31d0365.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationAssignmentChangesBusinessUnitData5aabf8e28cb310002520b2a2b31d0365`](./workday_staffing_python_sdk/pydantic/organization_assignment_changes_business_unit_data5aabf8e28cb310002520b2a2b31d0365.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}/businessUnit/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.update_comment`<a id="workdaystaffingorganization_assignment_changesupdate_comment"></a>

Partially updates the comment for the organization assignment change ID.
The {subResourceID} path parameter must be the same as the {ID} value.

The data updates in this PATCH method don't persist until you call POST/organizationAssignmentChanges/{ID}/submit.

To get the exising data to update, call GET/organizationAssignmentChanges/{ID}/comment/{subResourceID}.

Secured by: Change Organization Assignment (REST), Change Organization Assignments for  \~Worker\~ (Mass Action)

Scope: Organizations and Roles

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_comment_response = workdaystaffing.organization_assignment_changes.update_comment(
    body={
        "comment": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    comment="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### comment: `str`<a id="comment-str"></a>

The business process comment for a worker event before it's submitted.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Comments7d98fd55aeee100022968e52a1b31c60`](./workday_staffing_python_sdk/type/comments7d98fd55aeee100022968e52a1b31c60.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Comments7d98fd55aeee100022968e52a1b31c60`](./workday_staffing_python_sdk/pydantic/comments7d98fd55aeee100022968e52a1b31c60.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}/comment/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.update_cost_center`<a id="workdaystaffingorganization_assignment_changesupdate_cost_center"></a>

Partially updates the cost center for the specified organization assignment change ID. 
The {subResourceID} path parameter must be the same as the {ID} value.

You can call GET /organizationAssignmentChanges/{ID}/costCenter/{subResourceID} to get the existing data to update. 

The same Workday UI validations apply with this PATCH method. The data updates in this PATCH method do not persist until you call POST /organizationAssignmentChanges/{ID}/submit.

In the request body, specify the Workday ID of the cost center. 

To retrieve a costCenter ID, call the GET /values/organizationAssignmentChangesGroup/costCenters prompt endpoint, which takes the change organization assignment ID as the event query parameter. If you specify the event parameter, it returns HREF links to the cost centers by organization, as of the event's effective date. If you don't specify the event parameter, it returns HREF links to the cost centers by active organization based on the current date.

Secured by: Staffing Organizations: Cost Center

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_cost_center_response = workdaystaffing.organization_assignment_changes.update_cost_center(
    body={
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    cost_center=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### cost_center: `CostCenter5aabf8e28cb3100010a999f40b07024f`<a id="cost_center-costcenter5aabf8e28cb3100010a999f40b07024f"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrganizationAssignmentChangesCostCenterData5aabf8e28cb3100010a999db2700024e`](./workday_staffing_python_sdk/type/organization_assignment_changes_cost_center_data5aabf8e28cb3100010a999db2700024e.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationAssignmentChangesCostCenterData5aabf8e28cb3100010a999db2700024e`](./workday_staffing_python_sdk/pydantic/organization_assignment_changes_cost_center_data5aabf8e28cb3100010a999db2700024e.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}/costCenter/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.update_custom_organizations`<a id="workdaystaffingorganization_assignment_changesupdate_custom_organizations"></a>

Partially updates the custom organizations for the specified organization assignment change ID. 
The {subResourceID} path parameter must be the same as the {ID} value.

You can call GET /organizationAssignmentChanges/{ID}/customorganization/{subResourceID} to get the existing data to update. 

The same Workday UI validations apply with this PATCH method. The data updates in this PATCH method do not persist until you call POST /organizationAssignmentChanges/{ID}/submit.

In the request body, specify the Workday ID of the custom organization {id}

To retrieve a custom organization ID, call the GET /values/organizationAssignmentChangesGroup/customs prompt endpoint, which takes the change organization assignment ID as the event query parameter. If you specify the event parameter, it returns HREF links to the custom organizations, as of the event's effective date. If you don't specify the event parameter, it returns HREF links to the active custom organizations based on the current date.

Secured by: Staffing Organizations: Custom Organization

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_custom_organizations_response = workdaystaffing.organization_assignment_changes.update_custom_organizations(
    body={
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    custom_organizations=[
        {
            "descriptor": "Lorem ipsum dolor sit ame",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### custom_organizations: List[`CustomOrganizationDetails3950e273020a100017857926d35d369c`]<a id="custom_organizations-listcustomorganizationdetails3950e273020a100017857926d35d369c"></a>

The new custom organizations for the worker as of the effective date.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrganizationAssignmentChangesCustomOrganizationDetailsData53cd2b632146100011e9bf4e7041551f`](./workday_staffing_python_sdk/type/organization_assignment_changes_custom_organization_details_data53cd2b632146100011e9bf4e7041551f.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationAssignmentChangesCustomOrganizationDetailsData53cd2b632146100011e9bf4e7041551f`](./workday_staffing_python_sdk/pydantic/organization_assignment_changes_custom_organization_details_data53cd2b632146100011e9bf4e7041551f.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}/customOrganizations/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.organization_assignment_changes.update_region`<a id="workdaystaffingorganization_assignment_changesupdate_region"></a>

Partially updates the region for the specified organization assignment change ID. 

The {subResourceID} path parameter must be the same as the {ID} value.

In the request body, specify the Workday ID of the region. 

To retrieve a regions ID, call the GET /values/organizationAssignmentChangesGroup/regions prompt endpoint, which takes the change organization assignment ID as the event query parameter. If you specify the event parameter, it returns HREF links to the regions by organization, as of the event's effective date. If you don't specify the event parameter, it returns HREF links to the regions by active organization based on the current date.

Secured by: Staffing Organizations: Region

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_region_response = workdaystaffing.organization_assignment_changes.update_region(
    body={
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    region=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### region: `RegionA18edb56aca0100006997ec7e07d0374`<a id="region-regiona18edb56aca0100006997ec7e07d0374"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrganizationAssignmentChangesRegionDataA18edb56aca0100006997e68e5780373`](./workday_staffing_python_sdk/type/organization_assignment_changes_region_data_a18edb56aca0100006997e68e5780373.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationAssignmentChangesRegionDataA18edb56aca0100006997e68e5780373`](./workday_staffing_python_sdk/pydantic/organization_assignment_changes_region_data_a18edb56aca0100006997e68e5780373.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizationAssignmentChanges/{ID}/region/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.supervisory_organizations.get_by_id`<a id="workdaystaffingsupervisory_organizationsget_by_id"></a>

Retrieves a supervisory organization for the specified ID.

Secured by: BDA OAuth 2.0 Connector, Manage: Supervisory Organization, View: Supervisory Organization

Scope: Organizations and Roles

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = workdaystaffing.supervisory_organizations.get_by_id(
    include_inactive=True,
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### include_inactive: `bool`<a id="include_inactive-bool"></a>

If true, this method returns the inactive organizations. Default is false.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`SupervisoryOrganizationsGetByIdResponse`](./workday_staffing_python_sdk/pydantic/supervisory_organizations_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/supervisoryOrganizations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.supervisory_organizations.get_instance`<a id="workdaystaffingsupervisory_organizationsget_instance"></a>

Retrieves a supervisory organization for the specified ID.

Secured by: BDA OAuth 2.0 Connector, Manage: Supervisory Organization, View: Supervisory Organization

Scope: Organizations and Roles

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instance_response = workdaystaffing.supervisory_organizations.get_instance(
    id="ID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

#### 🔄 Return<a id="🔄-return"></a>

[`SupervisoryOrganizationViewA02c2e1916fa100009e137235f1f0018`](./workday_staffing_python_sdk/pydantic/supervisory_organization_view_a02c2e1916fa100009e137235f1f0018.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/supervisoryOrganizations/{ID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.supervisory_organizations.get_member`<a id="workdaystaffingsupervisory_organizationsget_member"></a>

Retrieves a member for the specified supervisory organization ID.

Secured by: Reports: Organization

Scope: Organizations and Roles

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_member_response = workdaystaffing.supervisory_organizations.get_member(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`JobData1bfa8925c50510000ae4479925510026`](./workday_staffing_python_sdk/pydantic/job_data1bfa8925c50510000ae4479925510026.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/supervisoryOrganizations/{ID}/members/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.supervisory_organizations.get_members`<a id="workdaystaffingsupervisory_organizationsget_members"></a>

Retrieves a collection of members for the specified supervisory organization ID.

Secured by: Reports: Organization

Scope: Organizations and Roles

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_members_response = workdaystaffing.supervisory_organizations.get_members(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`SupervisoryOrganizationsGetMembersResponse`](./workday_staffing_python_sdk/pydantic/supervisory_organizations_get_members_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/supervisoryOrganizations/{ID}/members` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.supervisory_organizations.get_org_chart`<a id="workdaystaffingsupervisory_organizationsget_org_chart"></a>

Retrieves information about an organization chart of the specified supervisory organization id.

Secured by: Reports: Organization

Scope: Organizations and Roles

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_org_chart_response = workdaystaffing.supervisory_organizations.get_org_chart(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`SupervisoryOrganizationsGetOrgChartResponse`](./workday_staffing_python_sdk/pydantic/supervisory_organizations_get_org_chart_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/supervisoryOrganizations/{ID}/orgChart` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.supervisory_organizations.get_org_chart_0`<a id="workdaystaffingsupervisory_organizationsget_org_chart_0"></a>

Retrieves information about an organization chart of the specified supervisory organization id.

Secured by: Reports: Organization

Scope: Organizations and Roles

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_org_chart_0_response = workdaystaffing.supervisory_organizations.get_org_chart_0(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`OrgChartView643e3a12629710000554e0338e670044`](./workday_staffing_python_sdk/pydantic/org_chart_view643e3a12629710000554e0338e670044.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/supervisoryOrganizations/{ID}/orgChart/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.create_check_in`<a id="workdaystaffingworkerscreate_check_in"></a>

Creates a single Check-In instance with the specified data with the specified worker. The worker is specified by the Workday ID of the worker.  You can use a returned id from GET /workers in the Staffing service /staffing.

In the request body, specify at least the required field: date. 
 
This endpoint is equivalent to the Create Check-In task in Workday.

Secured by: Worker Data: Check-Ins REST API

Scope: Performance Enablement

Contains attachment(s)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_check_in_response = workdaystaffing.workers.create_check_in(
    body={
        "description": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "date": "2024-03-23T07:00:00.000Z",
    },
    id="ID_example",
    description="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    associated_topics=[
        {
        }
    ],
    date="2024-03-23T07:00:00.000Z",
    check_in_attachments=[
        {
            "file_name": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
            "comment": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
            "file_length": 1171233711,
            "descriptor": "Lorem ipsum dolor sit ame",
        }
    ],
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### description: `str`<a id="description-str"></a>

Description of check-in.

##### associated_topics: List[`AssociatedCheckInTopicDetail316b5a26cc3c100010a01184c23902ea`]<a id="associated_topics-listassociatedcheckintopicdetail316b5a26cc3c100010a01184c23902ea"></a>

Topics included in a check-in.

##### date: `date`<a id="date-date"></a>

Date of check-in.

##### check_in_attachments: List[`CheckInAttachmentDetailEf244acfe6cf10002ebe92d43a7701d7`]<a id="check_in_attachments-listcheckinattachmentdetailef244acfe6cf10002ebe92d43a7701d7"></a>

Returns all attachments for the Check-In.

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CheckInDetail316b5a26cc3c10000ebdb0cb484602e1`](./workday_staffing_python_sdk/type/check_in_detail316b5a26cc3c10000ebdb0cb484602e1.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CheckInDetail316b5a26cc3c10000ebdb0cb484602e1`](./workday_staffing_python_sdk/pydantic/check_in_detail316b5a26cc3c10000ebdb0cb484602e1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/checkIns` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.create_check_in_topic`<a id="workdaystaffingworkerscreate_check_in_topic"></a>

Creates a single Check-In topic instance with the specified data with the specified worker. The worker is specified by the Workday ID of the worker.  You can use a returned id from GET /workers in the Staffing service /staffing.

In the request body, specify at least these required fields: name. 

This endpoint is equivalent to the Create Check-In Topic task in Workday.

Secured by: Worker Data: Check-Ins REST API

Scope: Performance Enablement

Contains attachment(s)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_check_in_topic_response = workdaystaffing.workers.create_check_in_topic(
    body={
        "shared_notes": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "private_notes": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "name": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    },
    id="ID_example",
    shared_notes="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    associated_check_ins=[
        {
        }
    ],
    private_notes="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    name="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    check_in_topic_attachments=[
        {
            "comment": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
            "file_name": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
            "file_length": 541229484,
            "descriptor": "Lorem ipsum dolor sit ame",
        }
    ],
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### shared_notes: `str`<a id="shared_notes-str"></a>

Shared notes of the topic.

##### associated_check_ins: List[`AssociatedCheckInDetail3267c0ba92a0100016ed105476ad03c4`]<a id="associated_check_ins-listassociatedcheckindetail3267c0ba92a0100016ed105476ad03c4"></a>

Check-ins associated to topic.

##### private_notes: `str`<a id="private_notes-str"></a>

Personal notes of the topic.

##### name: `str`<a id="name-str"></a>

Topic name.

##### check_in_topic_attachments: List[`CheckInTopicAttachmentDetail600ecde4c8421000278d06bfacea01c1`]<a id="check_in_topic_attachments-listcheckintopicattachmentdetail600ecde4c8421000278d06bfacea01c1"></a>

Returns all attachments for the Check-In Topic.

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CheckInTopicDetail3267c0ba92a010001688d79b032b03b8`](./workday_staffing_python_sdk/type/check_in_topic_detail3267c0ba92a010001688d79b032b03b8.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CheckInTopicDetail3267c0ba92a010001688d79b032b03b8`](./workday_staffing_python_sdk/pydantic/check_in_topic_detail3267c0ba92a010001688d79b032b03b8.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/checkInTopics` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.create_external_skill_levels`<a id="workdaystaffingworkerscreate_external_skill_levels"></a>

Creates external skill levels.

Secured by: Self-Service: External Skill Source, Worker Data: External Skill Source

Scope: Worker Profile and Skills

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_external_skill_levels_response = workdaystaffing.workers.create_external_skill_levels(
    body={
        "external_skill_level": 8,
        "external_skill_id": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "effective_moment": "2024-03-23T07:00:00.000Z",
        "context": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    },
    id="ID_example",
    external_skill_level=8,
    external_skill_id="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    effective_moment="2024-03-23T07:00:00.000Z",
    context="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### external_skill_level: `int`<a id="external_skill_level-int"></a>

The skill level normalized to a scale from 1-5 and to 1 decimal place.

##### external_skill_id: `str`<a id="external_skill_id-str"></a>

The skill from the external system.

##### effective_moment: `date`<a id="effective_moment-date"></a>

The date that the external Skill Level was last updated.

##### context: `str`<a id="context-str"></a>

The text you enter to provide context for this external skill load. Not visible to end users.

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExternalSkillLevelA39462f09c44100005d46fd77ef00000`](./workday_staffing_python_sdk/type/external_skill_level_a39462f09c44100005d46fd77ef00000.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ExternalSkillLevelA39462f09c44100005d46fd77ef00000`](./workday_staffing_python_sdk/pydantic/external_skill_level_a39462f09c44100005d46fd77ef00000.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/externalSkillLevel` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.create_home_contact_change_process`<a id="workdaystaffingworkerscreate_home_contact_change_process"></a>

Creates a new Home Contact Change business process event for the parent Person.

Secured by: Change Home Contact Information (REST Service)

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_home_contact_change_process_response = workdaystaffing.workers.create_home_contact_change_process(
    body={
        "href": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "effective_date": "2024-03-23T07:00:00.000Z",
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    href="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    effective_date="2024-03-23T07:00:00.000Z",
    id="string_example",
    descriptor="Lorem ipsum dolor sit ame",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### href: `str`<a id="href-str"></a>

The URL to the related change home contact information resource where this event can be interacted with via REST

##### effective_date: `date`<a id="effective_date-date"></a>

The date this business process takes effect.

##### id: `str`<a id="id-str"></a>

Id of the instance

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`HomeContactChangeEventF42ba27d87ed10001aa58a5d231b1621`](./workday_staffing_python_sdk/type/home_contact_change_event_f42ba27d87ed10001aa58a5d231b1621.py)
#### 🔄 Return<a id="🔄-return"></a>

[`HomeContactChangeEventF42ba27d87ed10001aa58a5d231b1621`](./workday_staffing_python_sdk/pydantic/home_contact_change_event_f42ba27d87ed10001aa58a5d231b1621.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/homeContactInformationChanges` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.create_skill_item`<a id="workdaystaffingworkerscreate_skill_item"></a>

Secured by: Person Data: Skills, Self-Service: Skills

Scope: Worker Profile and Skills

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_skill_item_response = workdaystaffing.workers.create_skill_item(
    body={
    },
    id="ID_example",
    skill_items=[
        {
            "skill_name": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
            "remote_id": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### skill_items: List[`SkillItemAddDefinitionFaed9891d75a10001e9a289910540228`]<a id="skill_items-listskillitemadddefinitionfaed9891d75a10001e9a289910540228"></a>

Exposes Skill Items for a Skill Qualification Enabled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SkillItemsBulkDefinition9d815bbfd67010000d6ed56204ab12de`](./workday_staffing_python_sdk/type/skill_items_bulk_definition9d815bbfd67010000d6ed56204ab12de.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SkillItemsBulkDefinition9d815bbfd67010000d6ed56204ab12de`](./workday_staffing_python_sdk/pydantic/skill_items_bulk_definition9d815bbfd67010000d6ed56204ab12de.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/skillItems` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.create_work_contact_information_changes`<a id="workdaystaffingworkerscreate_work_contact_information_changes"></a>

Creates a new Home Contact Change business process event for the parent Person.

Secured by: Change Work Contact Information (REST Service)

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_work_contact_information_changes_response = workdaystaffing.workers.create_work_contact_information_changes(
    body={
        "effective_date": "2024-03-23T07:00:00.000Z",
        "href": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    effective_date="2024-03-23T07:00:00.000Z",
    href="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    id="string_example",
    descriptor="Lorem ipsum dolor sit ame",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### effective_date: `date`<a id="effective_date-date"></a>

The date this business process takes effect.

##### href: `str`<a id="href-str"></a>

The URL to the related change work contact information resource where this event can be interacted with via REST.

##### id: `str`<a id="id-str"></a>

Id of the instance

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkContactChangeEvent5fca6c96c1c81000142fd03784140113`](./workday_staffing_python_sdk/type/work_contact_change_event5fca6c96c1c81000142fd03784140113.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WorkContactChangeEvent5fca6c96c1c81000142fd03784140113`](./workday_staffing_python_sdk/pydantic/work_contact_change_event5fca6c96c1c81000142fd03784140113.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/workContactInformationChanges` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.delete_check_in`<a id="workdaystaffingworkersdelete_check_in"></a>

Deletes an existing Check-In instance with the specified ID. This can only be done by the creater of the Check-In. 
 
This endpoint is equivalent to the Delete Check-In task in Workday.

Secured by: Self-Service: Check-Ins

Scope: Performance Enablement

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
workdaystaffing.workers.delete_check_in(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/checkIns/{subresourceID}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.delete_check_in_topic`<a id="workdaystaffingworkersdelete_check_in_topic"></a>

Deletes an existing Check-In topic instance with the specified ID. This can only be done by the creater of the Check-In topic. 

This endpoint is equivalent to the Delete Check-In Topic task in Workday.

Secured by: Self-Service: Check-Ins

Scope: Performance Enablement

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
workdaystaffing.workers.delete_check_in_topic(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/checkInTopics/{subresourceID}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.get_check_in`<a id="workdaystaffingworkersget_check_in"></a>

Retrieves a Check-In with the specified ID for the specified worker. The worker is specified by the Workday ID of the worker.  You can use a returned id from GET /workers in the Staffing service /staffing.

Secured by: Self-Service: Check-Ins, Worker Data: Check-Ins

Scope: Performance Enablement

Contains attachment(s)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_check_in_response = workdaystaffing.workers.get_check_in(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`CheckInsSummaryB3a69f47a499100010ce6be72bfe001d`](./workday_staffing_python_sdk/pydantic/check_ins_summary_b3a69f47a499100010ce6be72bfe001d.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/checkIns/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.get_check_in_topic`<a id="workdaystaffingworkersget_check_in_topic"></a>

Retrieves a Check-In topic with the specified ID for the specified worker. The worker is specified by the Workday ID of the worker.  You can use a returned id from GET /workers in the Staffing service /staffing.

Secured by: Self-Service: Check-Ins, Worker Data: Check-Ins

Scope: Performance Enablement

Contains attachment(s)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_check_in_topic_response = workdaystaffing.workers.get_check_in_topic(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`CheckInTopicsSummaryD81c816de26f10000ef2c5cb2fdd0015`](./workday_staffing_python_sdk/pydantic/check_in_topics_summary_d81c816de26f10000ef2c5cb2fdd0015.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/checkInTopics/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.get_check_in_topics`<a id="workdaystaffingworkersget_check_in_topics"></a>

Retrieves all Check-In topics for the specified worker. The worker is specified by the Workday ID of the worker.  You can use a returned id from GET /workers in the Staffing service /staffing.

Secured by: Self-Service: Check-Ins, Worker Data: Check-Ins

Scope: Performance Enablement

Contains attachment(s)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_check_in_topics_response = workdaystaffing.workers.get_check_in_topics(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkersGetCheckInTopicsResponse`](./workday_staffing_python_sdk/pydantic/workers_get_check_in_topics_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/checkInTopics` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.get_check_ins`<a id="workdaystaffingworkersget_check_ins"></a>

Retrieves all Check-Ins for the specified worker. The worker is specified by the Workday ID of the worker.  You can use a returned id from GET /workers in the Staffing service /staffing. 

This endpoint is equivalent to the View Check-Ins task in Workday.

Secured by: Self-Service: Check-Ins, Worker Data: Check-Ins

Scope: Performance Enablement

Contains attachment(s)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_check_ins_response = workdaystaffing.workers.get_check_ins(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkersGetCheckInsResponse`](./workday_staffing_python_sdk/pydantic/workers_get_check_ins_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/checkIns` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.get_collection_staffing`<a id="workdaystaffingworkersget_collection_staffing"></a>

Retrieves a collection of workers and current staffing information.

Secured by: Self-Service: Current Staffing Information, Worker Data: Public Worker Reports

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_collection_staffing_response = workdaystaffing.workers.get_collection_staffing(
    include_terminated_workers=True,
    limit=1,
    offset=1,
    search="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### include_terminated_workers: `bool`<a id="include_terminated_workers-bool"></a>

Include terminated workers in the output

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### search: `str`<a id="search-str"></a>

Searches workers by name or worker ID. The search is case-insensitive. You can include space-delimited search strings for an OR search.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkersGetCollectionStaffingResponse`](./workday_staffing_python_sdk/pydantic/workers_get_collection_staffing_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.get_explicit_skills`<a id="workdaystaffingworkersget_explicit_skills"></a>

Get Explicit Skills for Skill Enabled

Secured by: Person Data: Skills, Self-Service: Skills

Scope: Worker Profile and Skills

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_explicit_skills_response = workdaystaffing.workers.get_explicit_skills(
    id="ID_example",
    limit=1,
    offset=1,
    skill="string_example",
    skill_source="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### skill: `str`<a id="skill-str"></a>

Retrieves the skills for the specified skill name.

##### skill_source: `str`<a id="skill_source-str"></a>

The Workday ID of the skill source. Returns skills associated with the skill source.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkersGetExplicitSkillsResponse`](./workday_staffing_python_sdk/pydantic/workers_get_explicit_skills_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/explicitSkills` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.get_explicit_skills_for_skill_enabled`<a id="workdaystaffingworkersget_explicit_skills_for_skill_enabled"></a>

Get Explicit Skills for Skill Enabled

Secured by: Person Data: Skills, Self-Service: Skills

Scope: Worker Profile and Skills

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_explicit_skills_for_skill_enabled_response = workdaystaffing.workers.get_explicit_skills_for_skill_enabled(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`DisplayExplicitSkillRepresentationD6ca778018011000182fa5be1ae901a8`](./workday_staffing_python_sdk/pydantic/display_explicit_skill_representation_d6ca778018011000182fa5be1ae901a8.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/explicitSkills/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.get_external_skill_level`<a id="workdaystaffingworkersget_external_skill_level"></a>

Retrieves all external skill level information for a worker. You can filter the external skill levels by externalSkillId.

Secured by: Self-Service: External Skill Source, Worker Data: External Skill Source

Scope: Worker Profile and Skills

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_external_skill_level_response = workdaystaffing.workers.get_external_skill_level(
    id="ID_example",
    external_skill_id="string_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### external_skill_id: `str`<a id="external_skill_id-str"></a>

All External Skills. If passed, the External Skill Level associated with the External Skill ID.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkersGetExternalSkillLevelResponse`](./workday_staffing_python_sdk/pydantic/workers_get_external_skill_level_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/externalSkillLevel` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.get_external_skill_levels`<a id="workdaystaffingworkersget_external_skill_levels"></a>

Retrieves all external skill level information for a worker. You can filter the external skill levels by externalSkillId.

Secured by: Self-Service: External Skill Source, Worker Data: External Skill Source

Scope: Worker Profile and Skills

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_external_skill_levels_response = workdaystaffing.workers.get_external_skill_levels(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`ExternalSkillLevelDetail1c67ac98c0f310002706be33dcdb0000`](./workday_staffing_python_sdk/pydantic/external_skill_level_detail1c67ac98c0f310002706be33dcdb0000.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/externalSkillLevel/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.get_home_contact_change`<a id="workdaystaffingworkersget_home_contact_change"></a>

Retrieves an existing Home Contact Change event for the Person.

Secured by: Change Home Contact Information (REST Service)

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_home_contact_change_response = workdaystaffing.workers.get_home_contact_change(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`HomeContactChangeEventF42ba27d87ed10001aa58a5d231b1621`](./workday_staffing_python_sdk/pydantic/home_contact_change_event_f42ba27d87ed10001aa58a5d231b1621.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/homeContactInformationChanges/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.get_service_date`<a id="workdaystaffingworkersget_service_date"></a>

Retrieves information about a service date for the specified worker id.

Secured by: Self-Service: Service Dates, Worker Data: Service Dates

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_service_date_response = workdaystaffing.workers.get_service_date(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`ServiceDatesData6b1db753fd82100027b0c8519c860018`](./workday_staffing_python_sdk/pydantic/service_dates_data6b1db753fd82100027b0c8519c860018.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/serviceDates/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.get_service_dates`<a id="workdaystaffingworkersget_service_dates"></a>

Retrieves all service dates for the specified worker id.

Secured by: Self-Service: Service Dates, Worker Data: Service Dates

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_service_dates_response = workdaystaffing.workers.get_service_dates(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkersGetServiceDatesResponse`](./workday_staffing_python_sdk/pydantic/workers_get_service_dates_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/serviceDates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.get_skill_items`<a id="workdaystaffingworkersget_skill_items"></a>

Secured by: Person Data: Skills, Self-Service: Skills

Scope: Worker Profile and Skills

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_skill_items_response = workdaystaffing.workers.get_skill_items(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkersGetSkillItemsResponse`](./workday_staffing_python_sdk/pydantic/workers_get_skill_items_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/skillItems` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.get_skill_items_by_id`<a id="workdaystaffingworkersget_skill_items_by_id"></a>

Secured by: Person Data: Skills, Self-Service: Skills

Scope: Worker Profile and Skills

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_skill_items_by_id_response = workdaystaffing.workers.get_skill_items_by_id(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`SkillItemDisplayDefinition4b4b7d34b4a21000301eaf52086700d8`](./workday_staffing_python_sdk/pydantic/skill_item_display_definition4b4b7d34b4a21000301eaf52086700d8.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/skillItems/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.get_staffing_information`<a id="workdaystaffingworkersget_staffing_information"></a>

Retrieves a collection of workers and current staffing information.

Secured by: Self-Service: Current Staffing Information, Worker Data: Public Worker Reports

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_staffing_information_response = workdaystaffing.workers.get_staffing_information(
    id="ID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkerDataC2466b0778c610000d1936006720000e`](./workday_staffing_python_sdk/pydantic/worker_data_c2466b0778c610000d1936006720000e.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.get_work_contact_change`<a id="workdaystaffingworkersget_work_contact_change"></a>

Retrieves an existing Work Contact Change event for the Person.

Secured by: Change Work Contact Information (REST Service)

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_work_contact_change_response = workdaystaffing.workers.get_work_contact_change(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkContactChangeEvent5fca6c96c1c81000142fd03784140113`](./workday_staffing_python_sdk/pydantic/work_contact_change_event5fca6c96c1c81000142fd03784140113.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/workContactInformationChanges/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.initiate_job_change`<a id="workdaystaffingworkersinitiate_job_change"></a>

Initiates a job change request for a specific worker
Call this method to start a new job change event, which returns a new job change ID. Use the new ID to reference the job change event in subsequent methods that update or get information about the same event.

The same Workday UI validations apply with this POST method.  The updates in this POST method do not persist until you call POST /jobChanges/{ID}/submit.

In the request body, specify at least this required field: date, worker {id}, job {id}, reason {id}

To retrieve a worker ID, call the GET /values/jobChangesGroup/workers prompt endpoint with the effectiveDate query parameter. It returns HREF links to workers by category. You can filter the results by effectiveDate. By default, it returns workers on the current date. Only workers without blocking events or available for change job for the current user are returned.

To retrieve a job ID, call the GET /values/jobChangesGroup/jobs prompt endpoint with the worker query parameter.  It returns all positions for the worker with current user access to do a job change. You can filter the results by effectiveDate. By default, it returns positions on the current date. 

To retrieve a reason ID, call the GET /values/jobChangesGroup/reason prompt endpoint, which takes the job change ID as the staffingEvent query parameter. If you specify the staffingEvent parameter, it returns change job reasons for the staffingEvent, by the change job category. By default, it returns all change job categories and reasons.

To retrieve a supervisoryOrganization ID, call the GET /values/jobChangesGroup/supervisoryOrganization prompt endpoint, with proposedManager and effectiveDate query parameters. If you specify the proposedManager parameter, it returns HREF links to all supervisory organizations for that manager. If you specify effectiveDate, it filters the results by effective date. The default is the current date.

To retrieve a location ID, call the GET /values/jobChangesGroup/locations prompt endpoint, which takes the staffingEvent query parameter.  It returns HREF links to locations by location categories for the specified location. You can filter the results by effectiveDate. By default, it returns locations on the current date.

Secured by: Change Job (REST Service)

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
initiate_job_change_response = workdaystaffing.workers.initiate_job_change(
    body={
        "date": "2020-01-18T01:00:00.000Z",
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    supervisory_organization=None,
    location=None,
    template=None,
    reason=None,
    date="2020-01-18T01:00:00.000Z",
    job=None,
    id="string_example",
    descriptor="Lorem ipsum dolor sit ame",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### supervisory_organization: `SupervisoryOrganization75e528a78e9a10000ab75132a9df0116`<a id="supervisory_organization-supervisoryorganization75e528a78e9a10000ab75132a9df0116"></a>

##### location: `Location75e528a78e9a10000ab75125ebe50114`<a id="location-location75e528a78e9a10000ab75125ebe50114"></a>

##### template: `Template2b1b95dfe4af100007f63081aec5158e`<a id="template-template2b1b95dfe4af100007f63081aec5158e"></a>

##### reason: `Reason85deac43cd1a10000b96c80c118f171e`<a id="reason-reason85deac43cd1a10000b96c80c118f171e"></a>

##### date: `date`<a id="date-date"></a>

The date this business process takes effect.

##### job: `Job75e528a78e9a10000ab7512c5c550115`<a id="job-job75e528a78e9a10000ab7512c5c550115"></a>

##### id: `str`<a id="id-str"></a>

Id of the instance

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JobChangesStartDetailsPOSTData75e528a78e9a10000ab750ea156f0111`](./workday_staffing_python_sdk/type/job_changes_start_details_post_data75e528a78e9a10000ab750ea156f0111.py)
#### 🔄 Return<a id="🔄-return"></a>

[`JobChangesStartDetailsPOSTData75e528a78e9a10000ab750ea156f0111`](./workday_staffing_python_sdk/pydantic/job_changes_start_details_post_data75e528a78e9a10000ab750ea156f0111.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/jobChanges` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.initiate_organization_assignment_change`<a id="workdaystaffingworkersinitiate_organization_assignment_change"></a>

Initiates an organization assignment change for a specific worker.
Call this method to start a new change organization assignment event, which returns a new change organization assignment ID. Use the new ID to reference the change organization assignment event in subsequent methods that update or get information about the same event.

The same Workday UI validations apply with this POST method.  The updates in this POST method do not persist until you call POST /organizationAssignmentChanges/{ID}/submit.

In the request body, specify at least this required field: date, worker {id}, job {id}

To retrieve a worker ID, call the GET /values/organizationAssignmentChangesGroup/workers prompt endpoint with the effectiveDate query parameter. It returns HREF links to workers by category. You can filter the results by effectiveDate. By default, it returns workers on the current date. Only workers without blocking events or available for organization assignment change for the current user are returned.

To retrieve a job ID, call the /values/organizationAssignmentChangesGroup/jobs prompt endpoint with the worker query parameter.  It returns all positions for the worker with current user access to do an organization assignment change . You can filter the results by effectiveDate. By default, it returns positions on the current date.

Secured by: Change Organization Assignment (REST)

Scope: Organizations and Roles

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
initiate_organization_assignment_change_response = workdaystaffing.workers.initiate_organization_assignment_change(
    body={
        "date": "2024-03-23T07:00:00.000Z",
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    position=None,
    date="2024-03-23T07:00:00.000Z",
    id="string_example",
    descriptor="Lorem ipsum dolor sit ame",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### position: `Position99f6257185e61000043aadd66df203bb`<a id="position-position99f6257185e61000043aadd66df203bb"></a>

##### date: `date`<a id="date-date"></a>

The date this business process takes effect.

##### id: `str`<a id="id-str"></a>

Id of the instance

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrganizationAssignmentChangesPostCc45d62b623c1000132ac812c30a052e`](./workday_staffing_python_sdk/type/organization_assignment_changes_post_cc45d62b623c1000132ac812c30a052e.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationAssignmentChangesPostCc45d62b623c1000132ac812c30a052e`](./workday_staffing_python_sdk/pydantic/organization_assignment_changes_post_cc45d62b623c1000132ac812c30a052e.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/organizationAssignmentChanges` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.partially_update_check_in`<a id="workdaystaffingworkerspartially_update_check_in"></a>

Partially updates an existing Check-In instance with the specified ID and the specified data in the request body (archive). This can only be done by the creator or participant of the Check-In.
 
This endpoint is equivalent to the Archive Check-Ins task in Workday.

Secured by: Self-Service: Check-Ins, Worker Data: Check-Ins

Scope: Performance Enablement

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
partially_update_check_in_response = workdaystaffing.workers.partially_update_check_in(
    body={
        "archive": True,
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    archive=True,
    id="string_example",
    descriptor="Lorem ipsum dolor sit ame",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### archive: `bool`<a id="archive-bool"></a>

Indicates that the check-in is archived.

##### id: `str`<a id="id-str"></a>

Id of the instance

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CheckInArchiveDetail1163fe23102e10001df342088f8a018e`](./workday_staffing_python_sdk/type/check_in_archive_detail1163fe23102e10001df342088f8a018e.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CheckInArchiveDetail1163fe23102e10001df342088f8a018e`](./workday_staffing_python_sdk/pydantic/check_in_archive_detail1163fe23102e10001df342088f8a018e.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/checkIns/{subresourceID}?type&#x3D;archive` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.partially_update_check_in_topic`<a id="workdaystaffingworkerspartially_update_check_in_topic"></a>

Partially updates an existing Check-In topic instance with the specified ID and the specified data in the request body (name, privateNotes, sharedNotes, checkInTopicAttachments, or associatedCheckIns). This can only be done by the creator or participant of the Check-In. 

This endpoint is equivalent to the Edit Check-In Topic task in Workday.

Secured by: Self-Service: Check-Ins

Scope: Performance Enablement

Contains attachment(s)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
partially_update_check_in_topic_response = workdaystaffing.workers.partially_update_check_in_topic(
    body={
        "shared_notes": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "private_notes": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "name": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    shared_notes="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    associated_check_ins=[
        {
        }
    ],
    private_notes="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    name="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    check_in_topic_attachments=[
        {
            "comment": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
            "file_name": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
            "file_length": 541229484,
            "descriptor": "Lorem ipsum dolor sit ame",
        }
    ],
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### shared_notes: `str`<a id="shared_notes-str"></a>

Shared notes of the topic.

##### associated_check_ins: List[`AssociatedCheckInDetail3267c0ba92a0100016ed105476ad03c4`]<a id="associated_check_ins-listassociatedcheckindetail3267c0ba92a0100016ed105476ad03c4"></a>

Check-ins associated to topic.

##### private_notes: `str`<a id="private_notes-str"></a>

Personal notes of the topic.

##### name: `str`<a id="name-str"></a>

Topic name.

##### check_in_topic_attachments: List[`CheckInTopicAttachmentDetail600ecde4c8421000278d06bfacea01c1`]<a id="check_in_topic_attachments-listcheckintopicattachmentdetail600ecde4c8421000278d06bfacea01c1"></a>

Returns all attachments for the Check-In Topic.

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CheckInTopicDetail3267c0ba92a010001688d79b032b03b8`](./workday_staffing_python_sdk/type/check_in_topic_detail3267c0ba92a010001688d79b032b03b8.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CheckInTopicDetail3267c0ba92a010001688d79b032b03b8`](./workday_staffing_python_sdk/pydantic/check_in_topic_detail3267c0ba92a010001688d79b032b03b8.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/checkInTopics/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.save_user_skills`<a id="workdaystaffingworkerssave_user_skills"></a>

Save skills a user has

Secured by: Self-Service: Skills

Scope: Worker Profile and Skills

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
save_user_skills_response = workdaystaffing.workers.save_user_skills(
    body={
    },
    id="ID_example",
    skills=[
        {
            "remote_id": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
            "descriptor": "Lorem ipsum dolor sit ame",
        }
    ],
    skill_item=None,
    skill_sources=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### skills: List[`DisplayExplicitSkillRepresentationD6ca778018011000182fa5be1ae901a8`]<a id="skills-listdisplayexplicitskillrepresentationd6ca778018011000182fa5be1ae901a8"></a>

Explicit Skill Usages

##### skill_item: `SkillItem98f198f5056b100019631445471d225f`<a id="skill_item-skillitem98f198f5056b100019631445471d225f"></a>

##### skill_sources: List[`SkillItemSourceAddRepresentationC5fabc4ca81610000d5d15309ac90122`]<a id="skill_sources-listskillitemsourceaddrepresentationc5fabc4ca81610000d5d15309ac90122"></a>

Skill Sources

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateSkillUsageRepresentation98f198f5056b1000196313ffe9a0225e`](./workday_staffing_python_sdk/type/create_skill_usage_representation98f198f5056b1000196313ffe9a0225e.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreateSkillUsageRepresentation98f198f5056b1000196313ffe9a0225e`](./workday_staffing_python_sdk/pydantic/create_skill_usage_representation98f198f5056b1000196313ffe9a0225e.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/explicitSkills` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.update_check_in`<a id="workdaystaffingworkersupdate_check_in"></a>

Partially updates an existing Check-In instance with the specified ID and the specified data in the request body (date, description, or associated topics). This can only be done by the creator or participant of the Check-In. 
 
This endpoint is equivalent to the Edit Check-In task in Workday.

Secured by: Self-Service: Check-Ins

Scope: Performance Enablement

Contains attachment(s)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_check_in_response = workdaystaffing.workers.update_check_in(
    body={
        "description": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "date": "2024-03-23T07:00:00.000Z",
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    description="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    associated_topics=[
        {
        }
    ],
    date="2024-03-23T07:00:00.000Z",
    check_in_attachments=[
        {
            "file_name": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
            "comment": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
            "file_length": 1171233711,
            "descriptor": "Lorem ipsum dolor sit ame",
        }
    ],
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### description: `str`<a id="description-str"></a>

Description of check-in.

##### associated_topics: List[`AssociatedCheckInTopicDetail316b5a26cc3c100010a01184c23902ea`]<a id="associated_topics-listassociatedcheckintopicdetail316b5a26cc3c100010a01184c23902ea"></a>

Topics included in a check-in.

##### date: `date`<a id="date-date"></a>

Date of check-in.

##### check_in_attachments: List[`CheckInAttachmentDetailEf244acfe6cf10002ebe92d43a7701d7`]<a id="check_in_attachments-listcheckinattachmentdetailef244acfe6cf10002ebe92d43a7701d7"></a>

Returns all attachments for the Check-In.

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CheckInDetail316b5a26cc3c10000ebdb0cb484602e1`](./workday_staffing_python_sdk/type/check_in_detail316b5a26cc3c10000ebdb0cb484602e1.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CheckInDetail316b5a26cc3c10000ebdb0cb484602e1`](./workday_staffing_python_sdk/pydantic/check_in_detail316b5a26cc3c10000ebdb0cb484602e1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/checkIns/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.update_check_in_topic_state`<a id="workdaystaffingworkersupdate_check_in_topic_state"></a>

Partially updates an existing Check-In topic instance with the specified ID and the specified data in the request body (archive). This can only be done by the creator or participant of the Check-In. 

This endpoint is equivalent to the Archive Check-In Topic task in Workday.

Secured by: Self-Service: Check-Ins, Worker Data: Check-Ins

Scope: Performance Enablement

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_check_in_topic_state_response = workdaystaffing.workers.update_check_in_topic_state(
    body={
        "archive": True,
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    archive=True,
    id="string_example",
    descriptor="Lorem ipsum dolor sit ame",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### archive: `bool`<a id="archive-bool"></a>

Indicates that the topic is archived.

##### id: `str`<a id="id-str"></a>

Id of the instance

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CheckInTopicArchiveDetail1163fe23102e10001f72d77b213401a2`](./workday_staffing_python_sdk/type/check_in_topic_archive_detail1163fe23102e10001f72d77b213401a2.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CheckInTopicArchiveDetail1163fe23102e10001f72d77b213401a2`](./workday_staffing_python_sdk/pydantic/check_in_topic_archive_detail1163fe23102e10001f72d77b213401a2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/checkInTopics/{subresourceID}?type&#x3D;archive` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdaystaffing.workers.update_external_skill_level`<a id="workdaystaffingworkersupdate_external_skill_level"></a>

Updates external skill levels.

Secured by: Self-Service: External Skill Source, Worker Data: External Skill Source

Scope: Worker Profile and Skills

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_external_skill_level_response = workdaystaffing.workers.update_external_skill_level(
    body={
        "external_skill_level": 8,
        "external_skill_id": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "effective_moment": "2024-03-23T07:00:00.000Z",
        "context": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    external_skill_level=8,
    external_skill_id="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    effective_moment="2024-03-23T07:00:00.000Z",
    context="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### external_skill_level: `int`<a id="external_skill_level-int"></a>

The skill level normalized to a scale from 1-5 and to 1 decimal place.

##### external_skill_id: `str`<a id="external_skill_id-str"></a>

The skill from the external system.

##### effective_moment: `date`<a id="effective_moment-date"></a>

The date that the external Skill Level was last updated.

##### context: `str`<a id="context-str"></a>

The text you enter to provide context for this external skill load. Not visible to end users.

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExternalSkillLevelA39462f09c44100005d46fd77ef00000`](./workday_staffing_python_sdk/type/external_skill_level_a39462f09c44100005d46fd77ef00000.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ExternalSkillLevelA39462f09c44100005d46fd77ef00000`](./workday_staffing_python_sdk/pydantic/external_skill_level_a39462f09c44100005d46fd77ef00000.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/externalSkillLevel/{subresourceID}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
