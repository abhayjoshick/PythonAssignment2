import boto3

# def get_active_regions():
#     """Fetch all AWS regions where resources exist"""
    
#     ec2_client = boto3.client('ec2')
#     all_regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
    
#     active_regions = set()
    
#     for region in all_regions:
#         print(f"Checking region: {region}...")
        
#         # Check EC2 instances
#         ec2 = boto3.client('ec2', region_name=region)
#         if ec2.describe_instances()['Reservations']:
#             active_regions.add(region)
#             continue  # No need to check other services if EC2 exists
        
#         # Check RDS instances
#         rds = boto3.client('rds', region_name=region)
#         if rds.describe_db_instances()['DBInstances']:
#             active_regions.add(region)
#             continue
        
#         # Check S3 (global but include if any bucket exists)
#         s3 = boto3.client('s3')
#         if s3.list_buckets()['Buckets']:
#             active_regions.add(region)
    
#     return sorted(active_regions)

# # Fetch and print the regions
# regions_with_resources = get_active_regions()
# print("\nRegions where the customer has billed resources:")
# print(regions_with_resources)
def get_billed_regions():
    ce = boto3.client('ce')
    response = ce.get_cost_and_usage(
        TimePeriod={'Start': '2025-01-01', 'End': '2025-02-02'},
        Granularity='MONTHLY',
        Metrics=['BlendedCost'],
        GroupBy=[{'Type': 'DIMENSION', 'Key': 'REGION'}]
    )
    return [item['Keys'][0] for item in response['ResultsByTime'][0]['Groups']]

print(get_billed_regions())
