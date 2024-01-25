# Analyze the GitHub Usage Behavior of Python Developers with a High Number of Followers

## Content

<ul>
  <li><a href="/#Abstract">Abstract🚧(WIP)</a></li>
  <li><a href="/#Introduction">Introduction✅</a></li>
  <li><a href="/#Related-Work">Related Work🚧(WIP)</a></li>
  <li><a href="/#Data-Gathering">Data Gathering✅</a></li>
  <li><a href="/#Exploratory-Data-Analysis">Exploratory Data Analysis🚧(WIP)</a></li>
  <li><a href="/#Data-Analysis">Data Analysis🚧(WIP)</a></li>
  <li><a href="/#Results">Results🚧(WIP)</a></li>
  <li><a href="/#Conclusion">Conclusion🚧(WIP)</a></li>
  <li><a href="/#References">References🚧(WIP)</a></li>
</ul>

# Abstract

...

# Introduction

<ul>
  <li>This research involved the collection of data pertaining to the usage of GitHub by Python developers. The data was gathered by searching Google for keywords related to Python-related occupations, such as ‘Python programmer’, ‘Junior Python’, and ‘Senior Python’ etc.
  
  LinkedIn was utilized as the primary platform for this search, and through the exploration of multiple subdomains of LinkedIn, approximately 8,500 GitHub usernames were collected. Each individual user was then examined using the GitHub REST API.
  
  The objective of this research is to provide readers with insights into the behavior of Python developers with a high number of followers on GitHub. It is hoped that these insights can be applied to self-development studies, potentially providing a significant boost in one’s career, given that profiles with a high follower count are often more attractive to employers.
  </li>
</ul>

# Related Work

<ul>
  <li>
  <a href="/#1">[1]</a> presents the collection and mining of GitHub data with the aim to understand GitHub user behavior and project success factors by collecting information about approximately 100K projects and 10K GitHub users of these projects. They statistically analyzed the data, discretized values of features via the k-means algorithm, and the apriori algorithm to find out association rules.
    
  Project success was measured by the cardinality of downloads. They kept only the rules which had a download cardinality higher than a threshold of 1000 downloads. The results provide interesting insight into the GitHub ecosystem and seven success rules for GitHub projects.
  </li>
  <li>
    <a href="/#2">[2]</a> analyzed how developers use GitHub Actions and how several activity indicators change after their adoption.
    
  The adoption of GitHub Actions increases the number of monthly rejected pull requests and decreases the monthly number of commits on merged pull requests. These results are especially relevant for practitioners to understand and prevent undesirable effects on their projects. The study contributes to the understanding and anticipation of the effects of adopting such technology, which is important for planning and management.
  </li>
</ul>

# Data Gathering

<ul>
  <li>

  ## 1. Web Scraping

  <ul>

  <li>The first stage involved using Google to search for LinkedIn profiles of Python developers. A Python script was developed to automate the Google search process. The script was designed to automatically scroll to the bottom of the Google search results page and then manually click on the omitted results link if it was present. </li>
  
  <li>The search was conducted using specific keywords related to Python-related occupations, such as ‘Python Developer’ ‘Python programmer’, ‘Junior Python’, and ‘Senior Python’. The search was also conducted across multiple subdomains of LinkedIn. The search results were then manually selected, copied, and pasted into a text file for further processing.
  
Google Search Example: 
```
site:th.linkedin.com/in "github.com/" "contact" "python developer"
```
 </li>
  <li>This entire process cannot be fully automated since when Google detects unusual activity from an IP address, such as a high number of requests within a short period, it may suspect that the activity is being carried out by a bot. In such cases, Google will present a CAPTCHA challenge to verify that the user is human. This meant that the script had to be supervised and manually operated. </li>

  </ul>
    
  </li>

  <li>

  ## 2. Extracting GitHub Usernames

  <ul><li>The second stage involved extracting GitHub usernames. A Python function was developed to read the text file line by line, split each line into words, and check each word for the presence of ‘github.com/’. If ‘github.com/’ was found in a word, the word was cleaned to extract the GitHub username. The cleaning process involved removing the GitHub domain name, full stops, tildes, commas, quotation marks, parameters, forward slashes, and brackets. Incomplete usernames were ignored. The extracted usernames were then stored in a text file.</li></ul>
  
  </li>

  <li>

  ## 3. Requesting Data from GitHub API

  <ul><li>The third stage involved requesting data from the GitHub REST API. For each GitHub username, a request was sent to the GitHub REST API to retrieve the user’s profile data. This was done to ensure that the username corresponded to an actual user and not an organization or a user account that did not exist or had been removed. The usernames were also given aliases (e.g., usr1, usr2, …) to maintain privacy ethics.</li></ul>
  
  </li>

  <li>

  ## 4. Filtering and Splitting Usernames

  <ul><li>In the fourth stage, specifically for the purpose of gathering event data from the GitHub REST API, the usernames were filtered and split. The filtering was based on the ‘updated_at’ field in the user’s profile data. This field indicates the last time the user was active. Only users who had been active within the past 90 days were considered. This is because GitHub only retains user event data for the past 90 days.</li>

<li>The filtered usernames were then split into 28 datasets. This was done to overcome the event request limit (X-poll interval) of the GitHub API, which allows a certain number of requests per hour. By splitting the usernames into multiple datasets, the data gathering process could be run simultaneously on different devices, effectively bypassing the rate limit.</li>

<li>It’s important to note that this filtering and splitting process was only applied for the purpose of gathering event data. For the collection of starred and repo data, the non-filtered list of usernames was used.</li></ul>
  
  </li>

  <li>

  ## 5. Requesting Event, Starred and Repo Data

  <ul><li>The final stage involved requesting data about each user’s event, starred repositories and own repositories from the GitHub REST API. For each user, the latest 300 event activity, latest 100 starred repositories and latest 100 own repositories were requested.</li></ul>
  
  </li>
  
</ul>

# Exploratory Data Analysis

...

# Data Analysis

...

# Results

...

# Conclusion

...

# References
<ul>
  <li id="1">
    <a href="https://ieeexplore.ieee.org/document/7388026">[1] F. Chatziasimidis and I. Stamelos, “Data collection and analysis of GitHub repositories and users,” in 2015 6th International Conference on Information, Intelligence, Systems and Applications (IISA), Corfu, Greece, 2015, pp. 1-6, doi: 10.1109/IISA.2015.7388026.</a>
  </li>
  <li id="2">
    <a href="https://ieeexplore.ieee.org/document/9463074">[2] T. Kinsman, M. Wessel, M. A. Gerosa and C. Treude, “How Do Software Developers Use GitHub Actions to Automate Their Workflows?,” in 2021 IEEE/ACM 18th International Conference on Mining Software Repositories (MSR), Madrid, Spain, 2021, pp. 420-431. doi: 10.1109/MSR52588.2021.00054.</a>
</ul>
