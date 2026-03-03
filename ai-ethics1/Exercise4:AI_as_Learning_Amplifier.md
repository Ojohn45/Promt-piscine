# Phase 1: Build Foundation (you first)
answer = 
    🔹 First of all routing protocol decides how data travels from one device to anther across a netwok, so wireless routing protocol is about making unstable networks reliable, Saving energy,minimizing delay

# Wireless routing protocols are mainly grouped into three types:
answer = 
#    1️⃣ Proactive (Table-Driven) Protocols:
        🔹 This are network routing methods that mataining up to date consistently sending information from one node to another node in the network

#        Some Characteristic

            🟦 Constant Updates: Nodes periodically exchange sending information to keep tables current, even if they is no traffic.

            🟦 Low Latency: Since routes are pre-computed, packets can be sent immediately without waiting for route discovery.

            🟦 High Overhead: it continuously send periodic update messages, maintain full routing tables, share topology information with all nodes even if no one is sending actual data the route is never used

#    2️⃣ Reactive (On-Demand) Protocols:
        🔹 Reactive (On-Demand) Protocols are a class of routing protocols used in mobile ad hoc networks (MANETs) and wireless networks that discover, create, and maintain routes to the explexted destinations only when a source node needs to send data. So unlike Proactive (Table-Driven) Protocols these protocols consume less energy and bandwidth, and they also they avoid the constant, high-frequency control traffic required to maintain tables in proactive protocols but they have 3. Main Disadvantages high latency because the route must be discovered before data transmission, therfore there is a delay at the start of communication Examples: AODV, DSR, TORA.

#        Examples of Reactive (On-Demand) Protocols are
            🟦 Ad-hoc On-Demand Distance Vector (AODV)
            🟦 Dynamic Source Routing (DSR):
            🟦 Temporally Ordered Routing Algorithm (TORA) and
            🟦 Ad hoc On-Demand Multipath Distance Vector (AOMDV)

#    3️⃣ Hybrid Protocols:
        🔹 A hybrid protocol in computer networking is a routing protocol that combines the best compunents of both proactive and reactive routing strategies to achieve more clear, efficient and scalable data transfer, particularly in large-scale, dynamic network environments. It is also has high scalability meaning suitable for large networks and it also have low overhead, low latency and it is flexible but at the same time it is complex to configure out and it also requires higher memory and processing power for maintaining tables.

# Active reading, self-explanation (close the doc), simple scenario design (5–10 devices) with your justification.

#    1️⃣ Active Reading:
        🔹 I just not just reading passively but asking questions while reading and summarize sections nad also Highlight key ideas. while studing wireless routing protocols is wondered why Proactive (Table-Driven) Protocols is high overheaded and why Reactive (On-Demand) Protocols is better than proactive.

#    2️⃣ Self-Explanation (Close the Document):
        🔹 After reading about wireless routing protocols and it types i learned that it send in formation from one node ( which are computers, smartphone, printer,sever etc) to another, making unstable networks reliable, Saving energy,minimizing delay. I also learnt that some of the type of wireless routing protocols like proative send consistenly updated information from one node to anther it is fast because the route already known although reactive is more efficient and avoid bandwidth than proative in the sence that reactive is fatster than proactive and less stressfull.

#    3️⃣ Simple Scenario Design (5–10 Devices):
        🔹 Imagine 7 laptops (Laptop A, Laptop B, C, D to G respectfully) connected to a weak and unstable network and the laptops are sending and receving data. For instance if Laptop B,what to send data to Laptop E, it may use proactive or reactive method proactive which already has a already ready route to take when transfering the data and reactive create a route when there is a data transmition and three other Laptop C, G, and F respectfully, wants to still send data to each other too, and all Laptop are not in good range data so Laptop B, will look for the mos laptop that is in it's range maybe Laptop A is in the range of Laptop B it will send it to Laptop A and Laptop D is in the range of Laptop A it will send it to Laptop D and it will Loop trough each Laptop that is in the range of each other untill it comes to it apointed Laptop that it is originarily sent for. But they are challanged like the data may be loss deu to the weak signal, high latency if route often breakes and routing overhead. For me the most effective way to send data for this problem is reactive.

#    4️⃣ Justification
        🔹 For me the most effective way of tranfering data through this weak and unstable network is reactive protocol because although devices moves frequently, in reactive protocol Laptop B will send a route request to Laptop G, and when Laptop G resieves it, it will replies with a route and send it bach to Laptop B. This redueses less bandwidth no constant table updates, this way is better for unstable networks.

# Phase 2: Strategic AI Use

# Test your understanding, explore edge cases with targeted questions, then validat
answer = 
#    Explore Edge Cases:
     answer = 
       1️⃣ What if all intermediate nodes are out of range? → data cannot reach destination until a path appears.

       2️⃣ What if multiple laptops try to send data simultaneously? → potential congestion; reactive protocols may need multiple route discoveries.

       3️⃣ What if a node fails mid-transmission? → reactive protocols can discover alternate routes; proactive may rely on outdated tables.

#     Targeted Questions:
      answer =
#     1️⃣ Understanding Concepts:

        🟦 What is the main purpose of a wireless routing protocol?

        🟦 How does a node function in a wireless network?

        🟦 Why is proactive routing considered high overhead?

#    2️⃣ Scenario & Application:

        🟦 In your 7-laptop scenario, what would happen if Laptop A goes offline while forwarding data?

        🟦 How does a reactive protocol handle route failures differently from a proactive protocol?

        🟦 If all laptops are in weak range of each other, what challenges might arise for data transmission?

#    Validation:
     answer = 
     🔹 Basicly in wireless routing protocol it controls the flow of data or information across network from one wireless dives to another so to do that it use different ways, like proative protocol, reative protocol and hybride protocol these are the three main types of wireless routing protocol and each of these  type haves different ways of tranffering data or information.

# Phase 3: Real Application

# Question = Design a small smart-city network (1,000 IoT sensors, 50 traffic lights, 10 emergency vehicles). Decide protocols, justify choices, list failure points, then refine with AI feedback.

#   1,000 IoT SENSORS:
        🟦 PROTOCOL: 
            Hybride protocol.

        🟦 JUSTIFY CHOICES:
            Because uses low power, small data and it has low overhead.

#   50 TRAFFIC LIGHTS:
        🟦 PROTOCOL: 
            Proative protocol.

        🟦 JUSTIFY CHOICES:
            Because they is low delay, the route is stable and it has low latecy.

#   10 EMERGENCY VEHICLES:
        🟦 PROTOCOL:
            Reactive protocol.

        🟦 JUSTIFY CHOICES:
            Because it adapts to movement and changing topology.

#    FAILURE POINTS:
        🟦 What happens if 700 sensors send data at once?

        🟦 What if an emergency vehicle loses connection?

        🟦 What if interference your blocks signals?

#    AI FEEDBACK:
Here’s honest improvement advice:

1️⃣ Good Things

🔹 Correct protocol matching 👏

🔹 Logical reasoning

🔹 Clean separation of sections

🔹 Thinking about failure cases (very good)

2️⃣ Where You Can Improve

🔹 Be more specific in justification
Instead of “low power” or “low delay,” explain why that protocol achieves that.

🔹 Avoid short justifications
In design questions, 2–4 lines per section is stronger.

🔹 Expand failure analysis
Examiners like when you predict realistic engineering problems.

# Question = % human judgment vs. AI contribution:
answer = 
    🔹Haman judgment is 70-80% because of their understanding of problems,choosing protocols, thinking about what will go wrong all this atributes makes humans judgment are essential.
    🔹while AI Contribution is about 20-30% because they mostly help in refining of words, pointing out missing failure cases, and puting your answer in a better way that you haven't thaught about.

# Question = Could you defend decisions without AI?
amswer =
    🔹Yes i can, definetly.

# Question = What will you still remember in 6 months?
answer = 
    🔹If you are ever giving this kind of work you should do think cearfully before answering the question and when you deal with traffic lights you should use proative protocol and also know that it is because it has low delay for traffic route and it also has low latecy.

# Question = Did AI make you sharper, or think for you?
answer = 
    It did make it sharper, and it also showed me where i should walk on more