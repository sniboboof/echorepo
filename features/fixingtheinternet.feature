Feature: Client-Server Communication
    Send a simple message to a server that echoes the message
    
    Scenario: Send Message "Hello"
        Given the message "Hello"
        When i send the message
        Then the server echoes "Hello"