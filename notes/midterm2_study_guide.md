# Midterm 2 (Final) Study Guide

These are just representative questions of the kinds of topics you should know. You should study all the reading material and the supplemental books and site links in them.

1. What is an **application database** and what is an **integration database**? What are some concerns that one type has that the other does not?
2. What is the **Impendance Mismatch**?
3. What are the main two ways of dealing with an increase in application traffic? What are the tradeoffs?
4. What does the term NoSQL database refer to? What led to the emergence of these databases?
5. What are the different models of NoSQL databases, and what characterizes each?
6. What does the term **aggregate** refer to in the context of NoSQL databases? Provide some examples.
7. How do key-value stores and document databases differ in their approach to aggregate structures?
8. What is **sharding** and what is **replication**? How do they differ?
9. Describe the two main replication models (master-slave, peer-to-peer), their main advantages and disadvantages, and main use cases for each.
10. Peer-to-peer replication suffers from the possibility of inconsistent writes. Explain what that means and how it can be avoided.
11. Describe examples where inconsistent writes can be tolerated by the system.
12. Describe the **pessimistic** and **optimistic** approaches to conflict resolution.
13. Read-write conflicts can suffer from both *logical consistency* and *replication consistency*. Explain the difference between the two.
14. What does the **CAP theorem** say? What is its importance? Describe the meaning of the terms involved.
15. Describe different **quorum systems** with N=3 and with N=5, and their tradeoffs in terms of the CAP theorem (different values of W and R provide different features).
16. How can we avoid write-write conflicts in a quorum system? How can we avoid read-write conflicts?
17. What data model does MongoDb employ?
18. Describe the key possible stages in MongoDb's **aggregation** framework, and what each of them does. List at least 5 different stages.
19. What are the key stages in a map-reduce setting? Describe what happens in each stage.
20. Suppose we have a database of gpa scores and class year for all current Hanover students. We want to compute the average gpa for each class year. What would happen in each stage of a map-reduce solution to this problem?
21. What do the C-I-A initials stand for in the context of security? Also provide concrete examples.
22. What are the four groups that attack methods are usually classified in? Also provide concrete examples.
23. What is **identification** and what is **authentication**? What is the difference between the two?
24. What do we mean when we refer to **authentication factors**? What are the different factors? What are examples of each factor?
25. What is **multi-factor authentication**? Provide concrete examples.
26. What is **authorization**?
27. What is the **principle of least priviledge**? Also provide concrete examples.
28. What are the four different kinds of **access control**? Provide concrete examples.
29. What are **access control lists**? What are **capabilities**? How do they differ?
30. Describe in broad terms what **symmetric key ciphers** and **asymmetric key ciphers** are and what are the advantages and limitations of each.
31. What is a cryptographic hash function? What are some of its key properties?
32. Describe how **digital signing** happens, and what other cryptographic tools it uses.
33. Describe what a **digital certificate** is, how it works, and what problem it solves.
34. What are some important precautions to take when implementing a password-protected website?
35. The server digitally signs the sessionID when sending it to the user. Why?
