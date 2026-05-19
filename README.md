# Query Processing over Streaming Data Using Flink

This is a reproduction project of the official Cquirrel Demonstration\.

The original repos are:

Cquirrel\-release: https://github\.com/hkustDB/Cquirrel\-release; 

## Environment Requirement
### Operating System
Ubuntu Linux (tested on AutoDL Cloud Server)

### Software Dependencies

The experimental environment follows the official project configuration:

| Component    | Version   |
| ------------ | --------- |
| Python       | 3.8.5     |
| Java         | 1.8.0_261 |
| Scala        | 2.12.13   |
| Maven        | 3.6.3     |
| sbt          | 1.3.13    |
| yarn         | 1.22.10   |
| Apache Flink | 1.11.2    |

---

## Repository Structure

```text
.
├── core/                  # Core Cquirrel components
├── gui/                   # Flask backend + React frontend
├── script/                # Auxiliary scripts for project operation

├── configs/               # Query configuration files
├── generated/             # Generated Flink programs
├── DemoTools/             # TPC-H data generator
└── result/                # Storage directory for test running results
```

## Test Description

### Test Dataset

We adopt the standard TPC\-H benchmark dataset with three data scales:**0\.01 GB, 0\.1 GB, 1GB**\.

### Test SQL

**TPC\-H Query10** is used as the main test case in this reproduction\. We completed the whole process including SQL parsing, code generation and Flink task execution\.