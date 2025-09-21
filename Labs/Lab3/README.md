# Lab 3

## Team Members
- Shaurya Goel
- Vardhan Jain

## Lab Question Answers

Question 1: Why are RESTful APIs scalable?
    Answer: REST constraints (statelessness, uniform interface, caching, layered architecture) let servers be replicated behind load balancers; since each request is self-contained, any server can handle it, enabling horizontal scaling.
Question 2: According to the definition of "resources" provided in the AWS article above, What are the resources the mail server is providing to clients?
    Answer: The primary resource is **mail** (email objects). Optionally, mailboxes or collections of mail by sender/recipient are also resources.
Question 3: What is one common REST Method not used in our mail server? How could we extend our mail server to use this method?
    Answer: PUT/PATCH — can be used to update mail (e.g., mark as read). Implementation: add PUT /mail/<id> to accept JSON with fields to update.
Question 4: Why are API keys used for many RESTful APIs? What purpose do they serve? Make sure to cite any online resources you use to answer this question!
    API keys authenticate clients, enable rate limiting, billing/usage tracking, and reduce abuse; they identify who made the request and can be revoked. Cite: https://www.weatherapi.com/docs/