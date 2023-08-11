# Twitter-ETL-Airflow-AWS
This project showcases an Apache Airflow DAG that performs Extract, Transform, Load (ETL) on Twitter data using Twitter API v2. It leverages the power of AWS services, including EC2 for processing and S3 for storage, creating a seamless end-to-end data pipeline.

The `twitter_dag.py` script defines an Apache Airflow DAG for performing an Extract, Transform, Load (ETL) process on Twitter data. It fetches tweets from a specified user's timeline using Twitter API v2 and stores the refined data in an Amazon S3 bucket.

## Prerequisites

- Python 3.x installed.
- Apache Airflow installed.
- Twitter API keys and secrets obtained from your Twitter Developer account.
- Tweepy library installed (`pip install tweepy`).
- pandas library installed (`pip install pandas`).
- s3fs library installed (`pip install s3fs`).
- Amazon Web Services (AWS) account with access to EC2 and S3 services.
- Upgraded Twitter Developer account with access to Twitter API v2.

## Twitter API v2 and Pricing

This project is designed to work with Twitter API v2, as Twitter API v1 no longer supports extracting tweets. It's important to note that using Twitter API v2 might come with associated costs. Please refer to the [Twitter API Pricing](https://developer.twitter.com/en/pricing) page for information about pricing tiers and any potential fees.

## Configuration

1. Obtain Twitter API keys and secrets by creating a Twitter Developer account. Refer to the [Tweepy Documentation](http://docs.tweepy.org/en/stable/getting_started.html) for details on how to get your API credentials.

2. Create a `config.py` file in the same directory as `twitter_dag.py`. Add the following lines and replace the placeholders with your actual keys and secrets:

    ```python
    ACCESS_KEY = "your_access_key"
    ACCESS_SECRET = "your_access_secret"
    CONSUMER_KEY = "your_consumer_key"
    CONSUMER_SECRET = "your_consumer_secret"
    ```

3. Configure AWS credentials on your EC2 instance using IAM roles or AWS CLI.

## EC2 Setup and Configuration

1. Launch an EC2 instance with Ubuntu using your AWS account. Refer to the [AWS EC2 Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) for step-by-step instructions.

2. SSH into the EC2 instance and set up the required software, dependencies, and libraries for Airflow and your project.

## S3 Data Storage

1. Create an S3 bucket in your AWS account to store the refined tweet data. Refer to the [AWS S3 Documentation](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) for guidance on creating a bucket.

2. Configure appropriate access permissions for the S3 bucket and objects.

... (Rest of the document remains the same)

## DAG Configuration

1. Clone or download this repository to your EC2 instance.

2. Set up your Apache Airflow environment on the EC2 instance.

3. Place the `twitter_dag.py` file in your Airflow DAGs directory.

## DAG Execution

1. Access your Airflow web interface from your EC2 instance.

2. In the Airflow web UI, navigate to the "DAGs" section and locate the `twitter_dag` (or your chosen DAG name).

3. Toggle the DAG's state to "On" to activate it.

4. The DAG is configured to run daily. You can adjust the schedule interval in the DAG definition if needed.

## Task Details

- The DAG includes a single task (`run_twitter_etl_task`) that executes the `run_twitter_etl` function from the `twitter_etl` module.

## Customization

- Modify the `screen_name` variable in the `api.user_timeline()` function in the `run_twitter_etl` function to target a different Twitter user's timeline.

- Adjust other parameters in the DAG, ETL script, and AWS configurations to customize the data extraction, storage, and processing.

## Notes

- Ensure you comply with Twitter's API usage policies and guidelines.

- Monitor any rate limiting or API restrictions to avoid disruptions in data extraction.

- Follow security best practices for AWS services, including IAM roles, access control, and encryption.

## Resources

- [Tweepy Documentation](http://docs.tweepy.org/en/stable/getting_started.html) - Getting started with Tweepy API.

- [AWS EC2 Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) - Get started with Amazon EC2.

- [AWS S3 Documentation](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) - Create an Amazon S3 bucket.

## Author

[Erick Garcia](https://www.linkedin.com/in/erickmanalastasgarcia/)



