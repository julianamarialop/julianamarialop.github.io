---
title: "🚀 Continuous Integration and Continuous Delivery (CI/CD) in Azure Data Factory! 🔁✨"
slug: "continuous-integration-and-delivery-cicd-in-azure-data-factory"
date: 2023-10-12T13:00:00Z
summary: "CI is the practice of automatically testing every code change, while CD deploys those changes to staging or production systems. In Azure Data Factory, CI/CD involves moving pipelines between…"
tags: ["Azure", "Data Engineering"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/integra%C3%A7%C3%A3o-cont%C3%ADnua-e-entrega-cicd-azure-data-factory-lopes-9r2yf"
cover:
  image: cover.jpg
  alt: "🚀 Continuous Integration and Continuous Delivery (CI/CD) in Azure Data Factory! 🔁✨"
  relative: true
---

Today's topic is Data Factory + DevOps. Shall we take a look?

CI is the practice of automatically testing every code change, while CD deploys those changes to staging or production systems. In Azure Data Factory, CI/CD involves moving pipelines between different environments.

Here's how it works:

1️⃣ Developers create a feature branch to make changes and debug pipeline runs.

2️⃣ The changes are reviewed through pull requests and merged into the main branch.

3️⃣ The changes are then published to the development factory.

4️⃣ When they're ready, the changes are deployed to a test or UAT factory using Azure Pipelines.

5️⃣ After verification, the changes can be deployed to the production factory.

Best practices for CI/CD in Azure Data Factory:

✅ Configure Git integration only for the development factory.

✅ Use pre- and post-deployment scripts for tasks such as stopping/restarting triggers.

✅ Consider using a shared factory for integration runtimes across all stages.

✅ Carefully manage the deployment of private endpoints to avoid conflicts.

✅ Keep separate key vaults for different environments and use consistent secret names.

✅ Avoid spaces in resource names; use '\_' or '-' instead.

✅ Be careful when changing the repository to avoid errors.

✅ Use exposure control and feature flags to manage logic based on the environment.

❌ Remember that selectively publishing resources is not recommended because of dependencies.

Take care, and see you in the next article!
