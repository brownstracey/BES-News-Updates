News Update App
Overview
The News Update App is a web-based application that allows users to access the latest news articles from various categories and sources. The app integrates with a third-party news API to provide real-time news updates, offering users a personalized and interactive experience. Whether you're interested in global news, business, technology, or sports, the app helps you stay informed by presenting articles in an easy-to-read and organized format.

Key Features
1. Real-Time News Updates
The app fetches the latest news articles from multiple sources and categories in real time. Users can explore a wide range of topics, including world news, sports, technology, and business. This ensures that users always have access to up-to-date information.

2. Search Functionality
Users can search for specific news articles by keywords. Whether you're interested in a particular topic, event, or person, the search feature allows you to quickly find relevant news stories based on your query.

3. Category and Region Filters
The app provides several options to filter news by category (e.g., Technology, Sports, Business) and region (e.g., US, UK, Europe). This allows users to customize their news feed according to their interests and geographic preferences.

4. Sorting Articles
The app enables users to sort news articles by various criteria, such as:

Date: View the latest articles first.
Relevance: Sort by the most relevant articles based on the search query. This feature enhances the user experience by allowing them to easily navigate through large volumes of content.
5. User-Friendly Interface
The application has a clean and intuitive interface, designed for ease of use. Users can easily navigate between different sections, such as categories, search results, and specific articles. The app ensures that news is presented in a readable and accessible manner, regardless of the device or platform being used.

6. Seamless Load Balancing
The app is deployed across multiple web servers (Web01 and Web02), with a load balancer (Lb01) distributing incoming traffic. This setup ensures that the app can handle high traffic efficiently, providing reliable performance even during peak usage times.

7. Error Handling
The app gracefully handles API errors or downtime. If the external news API is unavailable, users are shown a user-friendly message indicating the issue. This ensures that the app remains functional and does not break under unexpected conditions.

How It Works
Fetching News: The app makes API calls to an external news service to fetch the latest articles. The API returns a list of news stories, which are then displayed in the app.

User Interaction: Once the news is displayed, users can:

Search: Enter keywords to find articles related to their interests.
Filter: Choose from different categories and regions to customize their news feed.
Sort: Sort the articles based on date or relevance.
Load Balancing: To ensure reliability and scalability, the app is deployed across two web servers. The load balancer distributes traffic between these servers, ensuring that users experience consistent performance regardless of server load.

Conclusion
The News Update App provides an interactive and customizable news experience, allowing users to stay informed with real-time updates. With features like search, filters, sorting, and seamless load balancing, the app ensures a smooth and personalized experience for every user.
