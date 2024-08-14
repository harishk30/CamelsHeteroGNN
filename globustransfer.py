import os
import subprocess
import time

 
# Define your Globus endpoint IDs and paths
source_endpoint_id = "58bdcd24-6590-11ec-9b60-f9dfb1abb183"  # Update with correct source ID
destination_endpoint_id = "dest_id"  # Update with correct destination ID
source_base_path = "/FOF_Subfind/Astrid/L25n256/LH/"
destination_base_path = "/Users/harishkrishnakumar/Desktop/NewData"  # Adjust this path

folders = [f"LH_{i}" for i in range(1000)]

def get_pending_jobs_count():
    # Check the number of pending (active or inactive) jobs
    list_command = "globus task list --filter-status ACTIVE --format unix --jmespath 'length(DATA)'"
    result = subprocess.run(list_command, shell=True, capture_output=True, text=True)
    pending_jobs_count = int(result.stdout.strip())
    return pending_jobs_count

# Throttle submission by batching
batch_size = 100
for i in range(0, len(folders), batch_size):
    batch = folders[i:i + batch_size]
    for folder in batch:
        while get_pending_jobs_count() >= 10:  # Adjust the threshold based on your limits
            print("Too many pending jobs, waiting...")
            time.sleep(10)
        source_file_path = os.path.join(source_base_path, folder, "groups_090.hdf5")
        destination_file_path = os.path.join(destination_base_path, f"groups_090_{folder}.hdf5")

        # Construct the Globus CLI command
        globus_command = f"globus transfer {source_endpoint_id}:{source_file_path} {destination_endpoint_id}:{destination_file_path}"

        # Execute the Globus transfer command
        subprocess.run(globus_command, shell=True, check=True)

    # Wait before submitting the next batch
    print(f"Batch {i // batch_size + 1} submitted, waiting for jobs to complete...")
    time.sleep(5)  # Wait for 5 minutes before submitting the next batch
