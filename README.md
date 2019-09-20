# Insight project directory

Anomalizer


• Context: Networks are constantly subjected to attacks which can effectively cripple a business' ability to function 
		○ Show 14:00-15:00 brute force attack on server
		○ These attacks are usually subtle and it is a problem to accurately identify them when they are taking place
		○ Anomalies
		
• Need: To detect but also distinguish anomalies from one another
		○ Not all anomalies are due to attacks
		○ Sometimes network behaves weird (people are weird)
		○ Costly active raise the alarm for every anomaly
		
• Dataset:
		○ Source: Canadian Institute of Cybersecurity Intrusion Detection Evaluation Dataset (CICID S2017)
		○ 5 days worth of network activity data / 4 days under attacks at different times
			§ Brute Force, Denial of Service, Heartbleed, Botnet etc
		○ Data Frame Snapshot (80 features, some measurements some engineered)
		
• Approach: Anomaly Detection
		○ Isolation Forests (also good for feature ranking)
		○ One class SVM
		○ Elliptic Envelope
		○ Clustering & Dimensionality Reduction (PCA, t-SNE)
