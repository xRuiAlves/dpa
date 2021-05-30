# Django Polls App + Django Cloud Deployer

This is a Django Polls web app that is highly based on the [Writing your first Django App tutorial](https://www.djangoproject.com/start/). It serves as part of the validation process of the [django-cloud-deployer](https://pypi.org/project/django-cloud-deployer/) plugin package that was developed as a Proof of Concept for a part of my Master's Degree thesis work.

Feel free to [try out the deployment](http://dpa.thesis.ruialves.me/).

## Implemented Changes

- Updated project requirements to feature the `django-cloud-deployer` package dependency
- Updated app's `urls.py` routes with `runInPaaS` and `runInFaaS` annotations

## Cloud Deployment Annotations - System Partitioning

The system's url endpoints were seperated (between PaaS and FaaS) as following:

- Running in FaaS:
    - Home page
    - `info/help/*` routes
    - `polls/*` routes (except for results)
- Running in PaaS:
    - `info/contacts/*` routes
    - `polls/:id/results/` routes

## Replicate this deployment

First, please refer to the [django-cloud-deployer](https://pypi.org/project/django-cloud-deployer/) package documentation.

- Install the requirements with `pip install -r requirements.txt`
- Configure the project:
    - Create a `.env` file with the required environment variables
    - Apply any required migrations with `python manage.py migrate`
- (*Optional*) Check which urls will run in which cloud service with the package's `check_deploy` command, with `python -m django_cloud_deployer check_deploy`
- Deploy the project with `python -m django_cloud_deployer deploy heroku azure`

## Notes and other regards

- The DNS configuration was made manually (it was out of the scope of the validation purposes) and is not part of the package deployment script as of now; However, it may be tackled as future work
