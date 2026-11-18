# Material Management Information System

## Overview

Material Management Information System designed to manage material master records, receiving transactions, issuance transactions, inventory monitoring, warehouse operations, and management reporting.

This project is based on actual materials management, inventory control, and warehouse monitoring experience gained from large-scale industrial and construction environments.

## Core Modules

### Material Master

- Material Code Management
- Material Description Management
- Unit of Measure Management
- Category Management
- Reorder Level Management

### Receiving Transactions

- Purchase Order Reference
- Receiving Records
- Quantity Received
- Date Received Tracking

### Issuance Transactions

- Issue Slip Processing
- Department Requests
- Material Issuance
- Quantity Tracking

### Inventory Monitoring

- Beginning Inventory
- Receipts
- Issues
- Ending Inventory
- Available Stock Monitoring

### Reporting

- Stock Card Report
- Receiving Report
- Issuance Report
- Inventory Summary Report
- Reorder Level Report

## System Workflow

Material Master

↓

Receiving Transactions

↓

Inventory Update

↓

Issuance Transactions

↓

Inventory Monitoring

↓

Management Reports

## Database Design

### Material Master Table

- material_id
- material_code
- material_description
- unit_of_measure
- category
- reorder_level

### Receiving Table

- receiving_id
- material_id
- date_received
- quantity_received
- po_number

### Issuance Table

- issuance_id
- material_id
- date_issued
- quantity_issued
- requestor
- department

## Technologies

### Original Systems

- Microsoft Access
- Visual FoxPro
- SQL
- Excel

### Modernized Version

- Python
- SQLite
- Pandas
- Excel
- Power BI

## Project Objectives

- Automate inventory transactions
- Improve stock monitoring
- Track material movements
- Support warehouse operations
- Generate management reports
- Provide business intelligence dashboards

## Future Enhancements

- Inventory Dashboard
- Stock Card Inquiry
- Reorder Monitoring
- Monthly Inventory Reporting
- Power BI Inventory Analytics

## Power BI Dashboard

The project includes a Power BI dashboard for inventory monitoring and warehouse management reporting.

### Dashboard Components

- Total Materials KPI
- Total Received KPI
- Total Issued KPI
- Current Stock KPI
- Current Stock by Material
- Reorder Level Monitoring
- Material Selection Filter

### Business Value

The dashboard provides management with visibility into inventory movements, current stock levels, material availability, and reorder requirements to support warehouse and procurement decisions.

## Author

Rollan P. Garcia

Database Developer | Power BI Developer | Data Analyst