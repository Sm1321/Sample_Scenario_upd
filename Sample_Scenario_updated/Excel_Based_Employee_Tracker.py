import streamlit as st
import pandas as pd
import os
import datetime
from PIL import Image
import datetime



# Display the image
# Open and resize the image
image = Image.open("SSA_Logo.jpg")
resized_image = image.resize((250, 90)) # Resize to 200x200 pixels
st.image(resized_image) # Display the resized image




# Define custom CSS for background color
page_bg = """
<style>
/* Apply background color to the entire Streamlit app */
.stApp {
    background-color: #f0f8ff; /* Light blue background */
}
</style>
"""
# Inject the CSS
#st.markdown(page_bg, unsafe_allow_html=True)

# Function to load data from CSV or create new DataFrame
#Here , we check if the CSV files are there or not , if not there , we can creet new and save it locally
def load_data():
    if os.path.exists('main_table.csv') and os.path.exists('employee_list.csv') and os.path.exists('project_list.csv') and os.path.exists('project_resource_table.csv'):
        # Load data from existing CSV files
        main_table = pd.read_csv('main_table.csv')
        employee_list = pd.read_csv('employee_list.csv')
        project_list = pd.read_csv('project_list.csv')
        project_resource_table = pd.read_csv('project_resource_table.csv')
    else:
        # Initialize default DataFrames
          # Initialize default DataFrames
        main_table = pd.DataFrame({
            'WeekEnd Date': ['2024-12-02', '2024-11-29', '2024-11-28', '2024-12-03', '2024-12-04'],
            'Employee Name': ['Ram', 'Laxman', 'Ram', 'Charan', 'Laxman'],
            'Project Name': ['Project A', 'Project B', 'Project C', 'Project D', 'Project E'],
            'Time(in hours)': [50, 60, 50, 80, 40]
        })

        employee_list = pd.DataFrame({
            'Employee Name': ['Ram', 'Laxman', 'Charan'],
            'Position': ['Analyst', 'Developer', 'Analyst'],
            'Skills': ['Python,Excel', 'Java, SQL', 'R, Analytics'],
            'CurrentStatus': ['Active', 'Active', 'Active']
        })

        project_list = pd.DataFrame({
            'Project Name': ['Project A', 'Project B', 'Project C', 'Project D', 'Project E'],
            'Description': ['Analysis', 'Development', 'Testing', 'Reporting', 'Design'],
            'Start Date': ['2024-12-02', '2024-11-29', '2024-11-28', '2024-12-03', '2024-12-04'],
            'Expected to Complete(Weeks)': [4, 6, 8, 3, 5],
            'Internal/External': ['Internal', 'External', 'Internal', 'External', 'Internal'],
            'Status': ['Active', 'Completed', 'On Hold', 'Active', 'Active']
        })

        # Initialize default DataFrame
        project_resource_table = pd.DataFrame({
            'Project Name': ['Project A', 'Project B', 'Project C', 'Project D', 'Project E'],
            'Resource': ['NAN', 'NAN', 'NAN', 'NAN', 'NAN'],
            'Role': ['Analyst', 'Developer', 'Tester', 'Developer', 'Analyst'],
            'Est_Time_Weeks': [4, 6, 8, 5, 3]
        })



        # Save the default DataFrames to CSV files
        #Here , it save locally , when we create it
        main_table.to_csv('main_table.csv', index=False)
        employee_list.to_csv('employee_list.csv', index=False)
        project_list.to_csv('project_list.csv', index=False)
        # Save the default DataFrame to a CSV file
        project_resource_table.to_csv('project_resource_table.csv', index=False)
        print("Default CSV files created and saved locally.")

    return main_table, employee_list, project_list,project_resource_table






# Function to save data to CSV
def save_data(main_table, employee_list, project_list,project_resource_table):
    main_table.to_csv('main_table.csv', index=False)
    employee_list.to_csv('employee_list.csv', index=False)
    project_list.to_csv('project_list.csv', index=False)
    project_resource_table.to_csv('project_resource_table.csv', index=False)

####################### Adding the infomation to the
# Helper functions to add data
def add_new_employee(Employee_Name, position, skills, current_status):
    new_employee = {'Employee Name':Employee_Name, 'Position': position, 'Skills': skills, 'CurrentStatus': current_status}
    employee_list.loc[len(employee_list)] = new_employee
    save_data(main_table, employee_list, project_list,project_resource_table) ##saving the Data

def add_new_project(project_name, description, start_date, total_hours,expected_completion, internal_or_external, status):
    new_project = {
        'Project Name': project_name,
        'Description': description,
        'Start Date': start_date,
        'Expected to Complete(Weeks)': expected_completion,
        'Total Hours':total_hours,
        'Internal/External': internal_or_external,
        'Status': status
    }
    project_list.loc[len(project_list)] = new_project
    save_data(main_table, employee_list, project_list,project_resource_table) ##saving the Data

def add_employee_work_details(start_date, employee_name, project_name, time_in_hours):
    new_work = {
        'WeekEnd Date': start_date,
        'Employee Name': employee_name,
        'Project Name': project_name,
        'Time(in hours)': time_in_hours
    }
    main_table.loc[len(main_table)] = new_work
    save_data(main_table, employee_list, project_list,project_resource_table) ##saving the Data

def add_project_resource_table(project, resource, role, est_time_weeks):
    new_row = {
        'Project Name': project,
        'Resource': resource,
        'Role': role,
        'Est_Time_Weeks': est_time_weeks
    }
    project_resource_table.loc[len(project_resource_table)] = new_row
    save_data(main_table, employee_list, project_list,project_resource_table) ##saving the Data

# Function to process and clean the data from the main table
# def main_table_data():
#     main_table['WeekEnd Date'] = pd.to_datetime(main_table['WeekEnd Date'])
#     # Extract year from 'WeekEnd Date'
#     main_table['Year'] = main_table['WeekEnd Date'].dt.year
#     # Convert year to string (if needed) and remove commas ,bcz of 2,024 to 2024
#     main_table['Year'] = main_table['Year'].astype(str).str.replace(",", "")
#     main_table['CY_WeekNumber'] = main_table['WeekEnd Date'].dt.isocalendar().week
   
#     main_table['Project_WeekNumber'] = (main_table['WeekEnd Date'] - project_list["Start Date"])
#     main_table['WeekEnd Date'] = main_table['WeekEnd Date'].dt.date #to remove the time stamp 00:00:00
#     return main_table


def main_table_data():
    # Ensure 'WeekEnd Date' is in datetime format
    main_table['WeekEnd Date'] = pd.to_datetime(main_table['WeekEnd Date'])

    # Ensure 'Start Date' in project_list is in datetime format
    project_list['Start Date'] = pd.to_datetime(project_list['Start Date'])

    # Extract year from 'WeekEnd Date'
    main_table['Year'] = main_table['WeekEnd Date'].dt.year

    # Convert year to string (if needed) and remove commas
    main_table['Year'] = main_table['Year'].astype(str).str.replace(",", "")

    # Calculate calendar year week number
    main_table['CY_WeekNumber'] = main_table['WeekEnd Date'].dt.isocalendar().week

    # Calculate project-specific week number
    main_table['Project_WeekNumber'] = (main_table['WeekEnd Date'] - project_list["Start Date"]).dt.days // 7

    # Remove timestamp from 'WeekEnd Date'
    main_table['WeekEnd Date'] = main_table['WeekEnd Date'].dt.date#to remove the time stamp 00:00:00
    # Remove timestamp from 'WeekEnd Date'
    project_list['Start Date'] = project_list['Start Date'].dt.date#to remove the time stamp 00:00:00

    return main_table



# Load data (from CSV or default values)
main_table, employee_list, project_list,project_resource_table = load_data()

# Streamlit app structure
st.sidebar.title("Choose your Task here")
option = st.sidebar.selectbox("Choose a section", 
    ["Dashboard", "Add New Employee", "Add New Project", "Employee Weekly Tracker","Add Project Resources", "Utilization Analysis","Actual Vs Estimated"])



# Dashboard Section
if option == "Dashboard":
    st.title("Employee Tracker Dashboard")
    #Output the Employee List Table
    st.header("Employee List")
    st.dataframe(employee_list, use_container_width=True)
    #Output the Main Table
    st.header(" Main Table")
    main_table = main_table_data()
    st.dataframe(main_table, use_container_width=True)
    #Output the Project List
    st.header("Project List")
    project_list["Start Date"] = pd.to_datetime(project_list ["Start Date"])
    st.dataframe(project_list, use_container_width=True)
    #Output the Resource Table
    st.header("Project Resource Table")
    st.dataframe(project_resource_table, use_container_width=True)

# Add New Employee Section
elif option == "Add New Employee":
    st.title("Add New Employee")
    with st.form(key='add_employee_form'):
        name = st.text_input("Name")
        position = st.text_input("Position")
        skills = st.text_input("Skills")
        current_status = st.selectbox("Current Status", ['Active', 'Inactive'])
        submit_employee = st.form_submit_button("Add Employee")
        if submit_employee:
            if name and position and skills and current_status:
                add_new_employee(name, position, skills, current_status)
                st.success("Employee added successfully!")
            else:
                st.error("Please fill all fields.")

# Add New Project Section
elif option == "Add New Project":
    st.title("Add New Project")
    with st.form(key='add_project_form'):
        project_name  = st.text_input("Project Name")
        description   = st.text_input("Description")
        start_date    = st.date_input("Start Date")
        expected_completion = st.number_input("Expected Completion (Weeks)", min_value=1)
        internal_or_external = st.selectbox("Internal or External", ['Internal', 'External'])
        status = st.selectbox("Status", ['Active', 'Completed', 'On Hold'])
        submit_project = st.form_submit_button("Add Project")
        if submit_project:
            if project_name and description and start_date and expected_completion and internal_or_external and status:
                add_new_project(project_name, description, start_date, expected_completion, internal_or_external, status)
                st.success("Project added successfully!")
            else:
                st.error("Please fill all fields.")

# Employee Weekly Tracker Section
elif option == "Employee Weekly Tracker":
    st.title("Employee Weekly Tracker")
    with st.form(key='add_work_form'):
        start_date      = st.date_input("Start Date")
        employee_name   = st.text_input("Employee Name")
        project_name    = st.text_input("Project Name")
        time_in_hours   = st.number_input("Time Spent (in hours)", min_value=1)
        submit_work     = st.form_submit_button("Add Work Details")
        if submit_work:
            if start_date and employee_name and project_name and time_in_hours:
                add_employee_work_details(start_date, employee_name, project_name, time_in_hours)
                st.success("Work details added successfully!")
            else:
                st.error("Please fill all fields.")

###ADd the project_resource_table
elif option == "Add Project Resources":
    st.title("Add Project Resources")
    with st.form(key='add_project_resources_form'):
        project_name = st.text_input("Enter  the Project Name")
        resource_name = st.text_input("Enter  the Resource Name")
        role_name = st.text_input("Enter  the Role")
        est_Time_in_Weeks = st.text_input(" Enter Estimated Time Weeks  ")
        submit_project_resources = st.form_submit_button("Add Project Resources")
        if submit_project_resources:
            if project_name and resource_name and  role_name and est_Time_in_Weeks:
                add_project_resource_table(project_name,resource_name,role_name,est_Time_in_Weeks)
                st.success("Added the Project Resources successfully!")
            else:
                st.error("Please fill all fields.")    

# Utilization Analysis Section
# Utilization Analysis Section 
elif option == "Utilization Analysis":
    st.title("Utilization Analysis")

    # Sidebar for options
    with st.sidebar:
        st.header("Select Option")

        # Main options select box
        main_option = st.selectbox("Choose an Option", ["Employee Work", "Filter Options"])

    # Load main table data
    #From the main tbale we will do all the analysis , okay
    filtered_data = main_table_data()

    # Employee Work Analysis
    if main_option == "Employee Work":
        st.subheader("Employee Work Analysis")

        # Create pivot table
        pivot_table = filtered_data.pivot_table(
            index = 'Employee Name',
            columns = 'Project Name',
            values = 'Time(in hours)',
            aggfunc = 'sum'  # Sum of hours worked by each employee on each project
        ).fillna(0)

        # Display pivot table
        st.dataframe(pivot_table, use_container_width = True)

    # Filter Options
    elif main_option == "Filter Options":
        st.write("### Select Filtering Options")

        # Checkboxes for filter options
        filter_by_date = st.sidebar.checkbox("Filter by Date")
        filter_by_year = st.sidebar.checkbox("Filter by Year")
        filter_by_project = st.sidebar.checkbox("Filter by Project")
        filter_by_week_number = st.sidebar.checkbox("Filter by Week Number")
        filter_by_employee_name = st.sidebar.checkbox("Filter by Employee Name")

        # Apply Date filter
        if filter_by_date:
            date_filter = st.date_input("Select Date", value=datetime.datetime.today())
            filtered_data = filtered_data[filtered_data['WeekEnd Date'] == date_filter]

        # Apply Year filter
        # Apply Year filter
        if filter_by_year:
            years = filtered_data['Year'].unique()  # Get unique years from the data
            years = list(years)  # Convert to a list if needed
            years.sort()  # Sort the years for better usability
            year_filter = st.selectbox("Select Year", options = years)  # Provide list as options
            filtered_data = filtered_data[filtered_data['Year'] == year_filter]


        # Apply Project filter (only if selected)
        if filter_by_project:
            projects = filtered_data['Project Name'].unique()  # Get unique project names
            projects = list(projects)  # Convert to list to insert "All Projects"
            projects.insert(0, "All Projects")  # Insert "All Projects" at the start
            project_filter = st.selectbox("Select Project", projects)  # Select project or "All Projects"

            # If "All Projects" is selected, don't filter by project
            if project_filter != "All Projects":
                filtered_data = filtered_data[filtered_data['Project Name'] == project_filter]

        # Apply Week Number filter
        if filter_by_week_number:
            week_number_filter = st.number_input("Select Week Number", min_value=1, max_value=53)
            filtered_data = filtered_data[filtered_data['CY_WeekNumber'] == week_number_filter]

        # Apply Employee Name filter (only if selected)
        if filter_by_employee_name:
            employee_names = filtered_data['Employee Name'].unique()  # Get unique employee names
            employee_names = list(employee_names)  # Convert to list to insert "All Employees"
            employee_names.insert(0, "All Employees")  # Insert "All Employees" at the start
            employee_name_filter = st.selectbox("Select Employee", employee_names)  # Select employee or "All Employees"

            # If "All Employees" is selected, don't filter by employee name
            if employee_name_filter != "All Employees": #This condition for other than ALL Employees
                filtered_data = filtered_data[filtered_data['Employee Name'] == employee_name_filter]

        # Display filtered data in a table
   
        st.dataframe(filtered_data, use_container_width=True)



  
##############-----------------------------------------------------------------------------------------------------------------------------------------
### Actual vs Predicted Option
elif option == "Actual Vs Estimated":
    # Load the main table data
    filtered_data = main_table_data()
    filter_by_project = st.sidebar.checkbox("Click here to Filter by Project")
    if filter_by_project:
        projects = filtered_data['Project Name'].unique()  # Get unique project names
        projects = list(projects)  # Convert to list to insert "All Projects"
        projects.insert(0, "All Projects")  # Insert "All Projects" at the start
        project_filter = st.sidebar.selectbox("Select Project", projects)  # Select project or "All Projects"

        if project_filter == "All Projects":
            #Table 1 :- Project Information
            Project_Information = project_list[["Project Name","Expected to Complete(Weeks)","Start Date","Total Hours"]]
            Project_Information = Project_Information ###COpy the DF
            Project_Information = Project_Information.rename(columns={"Expected to Complete(Weeks)": "Total Duration(Weeks)"})
            # the Project_Information is your DataFrame and the Start Date is in datetime format.
            Project_Information["Start Date"] = pd.to_datetime(Project_Information["Start Date"])
            # Calculate the End Date by adding the Total Duration (in weeks) to the Start Date
            Project_Information["End Date"] = Project_Information["Start Date"] + pd.to_timedelta(Project_Information["Total Duration(Weeks)"], unit="W")
            # Calculate Average Hours Per Week
            Project_Information["Average Hours Per Week"] = Project_Information["Total Hours"] / Project_Information["Total Duration(Weeks)"]
            # Calculate Average FTE/week
            Project_Information["Average FTE Per week"] = Project_Information["Average Hours Per Week"] / 40
           # Calculate weeks since start date
            current_date = datetime.datetime.today()
            Project_Information["Weeks since Start Date"] = (
                (pd.to_datetime(current_date) - Project_Information["Start Date"]).dt.days / 7
            ).clip(lower=0)

            # Calculate Total weeks elapsed till date
            Project_Information["Total weeks elapsed till date"] = Project_Information.apply(
                lambda row: row["Total Duration(Weeks)"]
                if row["Weeks since Start Date"] > row["Total Duration(Weeks)"]
                else 0,
                axis=1,
            )

            ###############################------------------------------#############################################
            # Calculate total hours spent per project
            #taking from the main table , the total hours spend on the each poject
            project_totals = main_table.groupby("Project Name")["Time(in hours)"].sum().reset_index()
            #chaning tha column name to match properly
            project_totals.rename(columns={"Time(in hours)": "Total hours spent till date"}, inplace=True)
            ##st.dataframe(project_totals)
            # Update "Total hours spent till date" in the detailed_projects table
            # Match "Project Name" between the two tables and map the hours
            Project_Information["Total hours spent till date"] = Project_Information["Project Name"].map(
                project_totals.set_index("Project Name")["Total hours spent till date"]
            )
            # Fill missing values with 0 for projects not in project_totals
            Project_Information["Total hours spent till date"] = Project_Information["Total hours spent till date"].fillna(0)
            ###############################------------------------------#############################################

            #Project_Information.drop(columns = ["Weeks since Start Date"],inplace = True) 
            # Display the dataframe
            Project_Information = Project_Information[["Project Name","Total Duration(Weeks)",	"Start Date","End Date","Total Hours","Average Hours Per Week",
                                                       	"Average FTE Per week","Weeks since Start Date",	"Total weeks elapsed till date","Total hours spent till date"]]
            Project_Information["End Date"] = Project_Information["End Date"].dt.date #to remove the time stamp 00:00:00
            Project_Information["Start Date"] = Project_Information["Start Date"].dt.date#to remove the time stamp 00:00:00
            st.subheader("1.Project Information")
            st.dataframe(Project_Information, use_container_width=True) 


            ###Table 2:- Project Summary
            st.subheader("2.Project Summary")
            project_summary = filtered_data[["Project Name","Project_WeekNumber","Time(in hours)"]]
            # Calculate current date
            current_date = datetime.datetime.today()
            # Convert the columns to datetime if not already
            filtered_data["WeekEnd Date"] = pd.to_datetime(filtered_data["WeekEnd Date"])
            project_list["Start Date"] = pd.to_datetime(project_list["Start Date"])
            #project_summary["Project_WeekNumber_1"] = main_table['WeekEnd Date']
            #project_summary["Project_WeekNumber_2"] = project_list["Start Date"]
            # Calculate the difference in days and then divide by 7 to get the week number
            project_summary["Project_WeekNumber"] = ((filtered_data["WeekEnd Date"] - project_list["Start Date"]).dt.days) // 7



            project_summary["Average Planned Hours"] = Project_Information["Total Hours"] / Project_Information["Total Duration(Weeks)"]
            # Display the dataframe
            st.dataframe(project_summary, use_container_width=True) 




            ###Table 3:- Main Table 
            st.subheader("3.Main Table Data")
            ###################################
            #adding filter if they select the ALL Projects to main table using group by
            #from the filter_data and doing mean by Timr(in hours)
            avg_work = filtered_data.groupby(["Project Name","Project_WeekNumber","Employee Name"])["Time(in hours)"].mean()
            st.dataframe(avg_work,use_container_width=True)



            st.subheader("4.Project Resouce Table")
            ###Table 4 Project Resource Table
            st.dataframe(project_resource_table,use_container_width=True)


########-----------------------------------------------------------------------------------------------------------------------------------------

        # Filter data based on selected project
        #here, the all projet names wiil be printed , so from this you can choose the project name
        if project_filter != "All Projects":
            filter_optiona_in_actual_vs_estimated = st.selectbox("Choose an Option", ["BY Employee Avg time(in hrs)","BY Week Date"])
            if filter_optiona_in_actual_vs_estimated == "BY Employee Avg time(in hrs)":
                #Table 1 :- Project Information
                Project_Information = project_list[["Project Name","Expected to Complete(Weeks)","Start Date","Total Hours"]]
                Project_Information = Project_Information ###COpy the DF
                Project_Information = Project_Information.rename(columns={"Expected to Complete(Weeks)": "Total Duration(Weeks)"})
                # the Project_Information is your DataFrame and the Start Date is in datetime format.
                Project_Information["Start Date"] = pd.to_datetime(Project_Information["Start Date"])
                # Calculate the End Date by adding the Total Duration (in weeks) to the Start Date
                Project_Information["End Date"] = Project_Information["Start Date"] + pd.to_timedelta(Project_Information["Total Duration(Weeks)"], unit="W")
                # Calculate Average Hours Per Week
                Project_Information["Average Hours Per Week"] = Project_Information["Total Hours"] / Project_Information["Total Duration(Weeks)"]
                # Calculate Average FTE/week
                Project_Information["Average FTE Per week"] = Project_Information["Average Hours Per Week"] / 40
            # Calculate weeks since start date
                current_date = datetime.datetime.today()
                Project_Information["Weeks since Start Date"] = (
                    (pd.to_datetime(current_date) - Project_Information["Start Date"]).dt.days / 7
                ).clip(lower=0)

                # Calculate Total weeks elapsed till date
                Project_Information["Total weeks elapsed till date"] = Project_Information.apply(
                    lambda row: row["Total Duration(Weeks)"]
                    if row["Weeks since Start Date"] > row["Total Duration(Weeks)"]
                    else 0,
                    axis=1,
                )

                ###############################------------------------------#############################################
                # Calculate total hours spent per project
                #taking from the main table , the total hours spend on the each poject
                project_totals = main_table.groupby("Project Name")["Time(in hours)"].sum().reset_index()
                #chaning tha column name to match properly
                project_totals.rename(columns={"Time(in hours)": "Total hours spent till date"}, inplace=True)
                ##st.dataframe(project_totals)
                # Update "Total hours spent till date" in the detailed_projects table
                # Match "Project Name" between the two tables and map the hours
                Project_Information["Total hours spent till date"] = Project_Information["Project Name"].map(
                    project_totals.set_index("Project Name")["Total hours spent till date"]
                )
                # Fill missing values with 0 for projects not in project_totals
                Project_Information["Total hours spent till date"] = Project_Information["Total hours spent till date"].fillna(0)
                ###############################------------------------------#############################################

                #Project_Information.drop(columns = ["Weeks since Start Date"],inplace = True) 
                # Display the dataframe
                Project_Information = Project_Information[["Project Name","Total Duration(Weeks)",	"Start Date","End Date","Total Hours","Average Hours Per Week",
                                                            "Average FTE Per week","Weeks since Start Date",	"Total weeks elapsed till date","Total hours spent till date"]]
                Project_Information["End Date"] = Project_Information["End Date"].dt.date #to remove the time stamp 00:00:00
                Project_Information["Start Date"] = Project_Information["Start Date"].dt.date#to remove the time stamp 00:00:00
                st.subheader("1.Project Information")
                Project_Information_filter_data = Project_Information[Project_Information['Project Name'] == project_filter]
                st.dataframe(Project_Information_filter_data, use_container_width=True) 
                #st.dataframe(Project_Information, use_container_width=True) 

                ###Table 2:- Project Summary
                st.subheader("2.Project Summary")
                project_summary = filtered_data[["Project Name","Project_WeekNumber","Time(in hours)"]]
                # Calculate current date
                current_date = datetime.datetime.today()
                # Convert the columns to datetime if not already
                filtered_data["WeekEnd Date"] = pd.to_datetime(filtered_data["WeekEnd Date"])
                project_list["Start Date"] = pd.to_datetime(project_list["Start Date"])
                #project_summary["Project_WeekNumber_1"] = main_table['WeekEnd Date']
                #project_summary["Project_WeekNumber_2"] = project_list["Start Date"]
                # Calculate the difference in days and then divide by 7 to get the week number
                project_summary["Project_WeekNumber"] = ((filtered_data["WeekEnd Date"] - project_list["Start Date"]).dt.days) // 7
                project_summary["Average Planned Hours"] = Project_Information["Total Hours"] / Project_Information["Total Duration(Weeks)"]
                # Display the dataframe
                project_summary_filter_data = project_summary[project_summary['Project Name'] == project_filter]
                st.dataframe(project_summary_filter_data, use_container_width=True) 
                # Display the dataframe
                #st.dataframe(project_summary, use_container_width=True) 

                ###This is the fiter option data --------------> BY Employee Avg time(in hrs)
                filtered_data = filtered_data[filtered_data['Project Name'] == project_filter]
                st.subheader("3.Employee Avg Work Details")    
                # Group by Employee Name and calculate the average work
                #This taken from the filtered_data(maintable)
                avg_work = filtered_data.groupby(["Project Name","CY_WeekNumber","Employee Name"])["Time(in hours)"].mean()
                st.dataframe(avg_work,use_container_width=True)

            elif filter_optiona_in_actual_vs_estimated =="BY Week Date":
                #Table 1 :- Project Information
                Project_Information = project_list[["Project Name","Expected to Complete(Weeks)","Start Date","Total Hours"]]
                Project_Information = Project_Information ###COpy the DF
                Project_Information = Project_Information.rename(columns={"Expected to Complete(Weeks)": "Total Duration(Weeks)"})
                # the Project_Information is your DataFrame and the Start Date is in datetime format.
                Project_Information["Start Date"] = pd.to_datetime(Project_Information["Start Date"])
                # Calculate the End Date by adding the Total Duration (in weeks) to the Start Date
                Project_Information["End Date"] = Project_Information["Start Date"] + pd.to_timedelta(Project_Information["Total Duration(Weeks)"], unit="W")
                # Calculate Average Hours Per Week
                Project_Information["Average Hours Per Week"] = Project_Information["Total Hours"] / Project_Information["Total Duration(Weeks)"]
                # Calculate Average FTE/week
                Project_Information["Average FTE Per week"] = Project_Information["Average Hours Per Week"] / 40
            # Calculate weeks since start date
                current_date = datetime.datetime.today()
                Project_Information["Weeks since Start Date"] = (
                    (pd.to_datetime(current_date) - Project_Information["Start Date"]).dt.days / 7
                ).clip(lower=0)

                # Calculate Total weeks elapsed till date
                Project_Information["Total weeks elapsed till date"] = Project_Information.apply(
                    lambda row: row["Total Duration(Weeks)"]
                    if row["Weeks since Start Date"] > row["Total Duration(Weeks)"]
                    else 0,
                    axis=1,
                )

                ###############################------------------------------#############################################
                # Calculate total hours spent per project
                #taking from the main table , the total hours spend on the each poject
                project_totals = main_table.groupby("Project Name")["Time(in hours)"].sum().reset_index()
                #chaning tha column name to match properly
                project_totals.rename(columns={"Time(in hours)": "Total hours spent till date"}, inplace=True)
                ##st.dataframe(project_totals)
                # Update "Total hours spent till date" in the detailed_projects table
                # Match "Project Name" between the two tables and map the hours
                Project_Information["Total hours spent till date"] = Project_Information["Project Name"].map(
                    project_totals.set_index("Project Name")["Total hours spent till date"]
                )
                # Fill missing values with 0 for projects not in project_totals
                Project_Information["Total hours spent till date"] = Project_Information["Total hours spent till date"].fillna(0)
                ###############################------------------------------#############################################

                #Project_Information.drop(columns = ["Weeks since Start Date"],inplace = True) 
                # Display the dataframe
                Project_Information = Project_Information[["Project Name","Total Duration(Weeks)",	"Start Date","End Date","Total Hours","Average Hours Per Week",
                                                            "Average FTE Per week","Weeks since Start Date",	"Total weeks elapsed till date","Total hours spent till date"]]
                Project_Information["End Date"] = Project_Information["End Date"].dt.date #to remove the time stamp 00:00:00
                Project_Information["Start Date"] = Project_Information["Start Date"].dt.date#to remove the time stamp 00:00:00
                st.subheader("1.Project Information")
                ##Applying filter based on the selected project from project_list
                ###filtered_data = filtered_data[filtered_data['Project Name'] == project_filter]
                Project_Information_filter_data = Project_Information[Project_Information['Project Name'] == project_filter]
                st.dataframe(Project_Information_filter_data, use_container_width=True) 



                 ###Table 2:- Project Summary
                st.subheader("2.Project Summary")
                project_summary = filtered_data[["Project Name","Project_WeekNumber","Time(in hours)"]]
                # Calculate current date
                current_date = datetime.datetime.today()
                # Convert the columns to datetime if not already
                filtered_data["WeekEnd Date"] = pd.to_datetime(filtered_data["WeekEnd Date"])
                project_list["Start Date"] = pd.to_datetime(project_list["Start Date"])
                #project_summary["Project_WeekNumber_1"] = main_table['WeekEnd Date']
                #project_summary["Project_WeekNumber_2"] = project_list["Start Date"]
                # Calculate the difference in days and then divide by 7 to get the week number
                project_summary["Project_WeekNumber"] = ((filtered_data["WeekEnd Date"] - project_list["Start Date"]).dt.days) // 7



                project_summary["Average Planned Hours"] = Project_Information["Total Hours"] / Project_Information["Total Duration(Weeks)"]
                # Display the dataframe
                project_summary_filter_data = project_summary[project_summary['Project Name'] == project_filter]
                st.dataframe(project_summary_filter_data, use_container_width=True) 
                ###st.dataframe(project_summary, use_container_width=True) 



                ############ ------------->BY Week Date
                ############################################## MAin table######################
                filtered_data = filtered_data[filtered_data['Project Name'] == project_filter]
                st.subheader("3.Main Table Data")
                # Remove timestamp from 'WeekEnd Date'
                filtered_data ['WeekEnd Date'] = filtered_data ['WeekEnd Date'].dt.date#to remove the time stamp 00:00:00
                st.dataframe(filtered_data,use_container_width=True)

            #No filter for the resource table 
            #This will be printed for thr both if or else
            filtered_project_resource_table = project_resource_table[project_resource_table['Project Name']== project_filter]
            st.subheader("4.Project Resouce Table")
            st.dataframe(filtered_project_resource_table,use_container_width=True)






