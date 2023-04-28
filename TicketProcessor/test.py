from TicketProcessor.prompt import processUserQuery
import TicketProcessor.parseResp as parseResp

response= processUserQuery("how to restart computer?")

print(response)
print(parseResp.parse(response))

