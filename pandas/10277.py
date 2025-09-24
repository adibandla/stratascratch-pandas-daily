# https://platform.stratascratch.com/coding/10277-find-all-inspections-which-are-part-of-an-inactive-program?code_type=2
# Find all inspections which are part of an inactive program

# <los_angeles_restaurant_health_inspections>
# serial_number		object
# activity_date		datetime64[ns]
# facility_name		object
# score				int64
# grade				object
# service_code		int64
# service_description	object
# employee_id			object
# facility_address	object
# facility_city		object
# facility_id			object
# facility_state		object
# facility_zip		object
# owner_id			object
# owner_name			object
# pe_description		object
# program_element_pe	int64
# program_name		object
# program_status		object
# record_id			object

# import libraries
import pandas as pd

# code
los_angeles_restaurant_health_inspections.head()
los_angeles_restaurant_health_inspections[
    los_angeles_restaurant_health_inspections['program_status'] == 'INACTIVE'
    ]
