# Cquirrel Reproduction

This is a reproduction project of the official Cquirrel Demonstration\.

The original repos are:

Cquirrel\-release: https://github\.com/hkustDB/Cquirrel\-release; 

Cquirrel\-frontend:https://github\.com/hkustDB/Cquirrel\-Frontend; 

## Environment Requirement

### Operating System

This reproduction is deployed on Linux \(AutoDL Cloud Server\), breaking the original MacOS\-only limitation\.

### Software Dependencies

Consistent with the official experimental environment:

- Python 3\.8\.5

- Java 1\.8\.0\_261

- Scala 2\.12\.13

- Maven 3\.6\.3

- sbt 1\.3\.13

- yarn 1\.22\.10

- Flink 1\.11\.2

## Directory Description

- `DemoTools/DataGenerator` : Tool for generating TPC\-H input datasets\.

- `codegen` : Core component that transforms SQL into Flink programs\.

- `gui` : Web visualization module, including Flask backend and React frontend\.

- `script` : Auxiliary scripts for project operation\.

- `result` : Storage directory for test running results\.

- `generated\-code\-xxx` : Generated Flink code of TPC\-H Query10 under different data scales \(sf0\.01/sf0\.1/sf1\)\.

- `generated\_q10\.json` : SQL configuration file for Query10 test\.

- `cquirrel\-core\-1\.0\-SNAPSHOT\.jar` : Core dependency package of Cquirrel\.

## Test Description

### Test Dataset

We adopt the standard TPC\-H benchmark dataset with three data scales:**0\.01 GB, 0\.1 GB, 1GB**\.

### Test SQL

**TPC\-H Query10** is used as the main test case in this reproduction\. We completed the whole process including SQL parsing, code generation and Flink task execution\.