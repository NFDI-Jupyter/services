# Credits

Jupyter4NFDI provides access to powerful, flexible computing resources offered by different research institutions across Germany. To ensure that all users can benefit fairly from these shared resources, Jupyter4NFDI introduces a **credit-based resource usage system**.

This system helps prevent situations where a small number of users consume the majority of the available resources. Instead, credits allow for a balanced and predictable usage model where everyone receives an equitable opportunity to work with large compute environments.

---

## What Are Credits?

Credits represent a user's ability to start and run computing environments (called *Flavors*) on a Jupyter4NFDI system.  
Every user receives an allocation of credits. As long as credits are available, users can continue running sessions on the platform.

The **amount of credits you receive may depend on your selected AAI (Authentication and Authorization Infrastructure)** ([more](../authentication.md)). Different AAIs may lead to different credit budgets.

---

## How Credit Consumption Works

When you start a session on Jupyter4NFDI, you choose a **Flavor**, which defines the amount of CPU, memory, storage, or GPUs your environment will have.  
Credit consumption is tied directly to this choice:

- Lightweight Flavors consume fewer credits over time.
- Large or GPU-enabled Flavors consume credits at a faster rate.
- Credits are deducted continuously while your session is running.

If your credits reach zero, sessions will be stopped automatically. 
You will receive new credits every few hours.

---

## Project-Based Credits

Jupyter4NFDI supports collaboration through **Projects**.  
A Project is a shared credit pool that can be used by multiple researchers. This is particularly useful in situations such as:

- Research teams working on joint analyses  
- Organized workshops  
- Communities using Jupyter4NFDI as shared infrastructure  

When you are a member of a Project:

1. Your resource usage first deducts credits from the **Project pool**.
2. Only if the Project credits are exhausted will your **personal credits** be used.

This ensures collaborative work is not limited by individual user budgets and creates a seamless environment for group-based scenarios.

If your team needs additional credits, you can contact us and request a Project.

---

## Per-System Credit Allocation

Jupyter4NFDI operates across multiple resource providers.  
Each provider manages its own credit configuration, meaning:

- You may see different credit amounts depending on the system you access.
- Some systems may offer higher or lower credit budgets.
- Providers can adjust credit allocations and consumption rates over time, depending on load, hardware availability, or policy changes.

Your displayed credit amounts and consumption are therefore **system-specific**.

---

## Summary

The Jupyter4NFDI Credit System ensures a fair, transparent, and flexible way of distributing computational resources. Users benefit by:

- Avoiding resource monopolization by heavy users  
- Being able to plan usage based on predictable credit consumption  
- Collaborating through shared Project credit pools  
- Accessing multiple systems with different credit configurations  

If you have questions about your credits, Flavors, or how to request a Project, please contact us.
