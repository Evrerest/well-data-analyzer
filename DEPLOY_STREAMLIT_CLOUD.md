# Deploy To Streamlit Community Cloud

This app is ready to deploy publicly on Streamlit Community Cloud.

## What you need

- A GitHub account
- A public GitHub repository containing this project
- A Streamlit Community Cloud account connected to GitHub

Official references:

- https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app
- https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy
- https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies

## Repository requirements

This repo already has the important pieces:

- `app.py` as the entrypoint
- `requirements.txt` for Python dependencies

You do not need the Windows executable files for cloud deploys.

## Deploy steps

1. Push this project to a public GitHub repository.
2. Go to `https://share.streamlit.io`.
3. Click `Create app`.
4. Choose your repository and branch.
5. Set the entrypoint file to `app.py`.
6. Optionally choose a custom subdomain.
7. In Advanced settings, set Python version to `3.12`.
8. Click `Deploy`.

## Expected behavior after deploy

- The app will be public by default if the repository is public.
- Updates pushed to GitHub will automatically redeploy.
- Testers can open the app in a browser with no install step.

## Notes For Later

- If you want login later, we can add authentication in front of the app.
- If you want private access later, Community Cloud also supports changing app sharing settings.
- If uploaded data becomes sensitive, we should revisit whether public hosting is still the right choice.
