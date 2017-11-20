from datetime import datetime
from pytz import timezone
from pyexchange import Exchange2010Service, ExchangeNTLMAuthConnection
from Event import Event

originURL = u'https://nomeDoServidor.outlook.com/EWS/Exchange.asmx'
originUsername = u'nomeDoUsuario'
originPassword = u"passwordDoUsuario"

# Set up the connection to Exchange
originConnection = ExchangeNTLMAuthConnection(url=originURL,
                                        username=originUsername,
                                        password=originPassword)

originService = Exchange2010Service(originConnection)

originCalendar = originService.calendar()

originEvents = originCalendar.list_events(
    start=timezone("America/Sao_Paulo").localize(datetime(2017, 11, 1, 0, 0, 0)),
    end=timezone("America/Sao_Paulo").localize(datetime(2017, 11, 17, 0, 0, 0)),
    details=True
)


destinyURL = u'https://outroServidor.outlook.com/EWS/Exchange.asmx'
destinyUsername = u'nomeUsuario'
originPassword = u'passwordUsuario'

# Set up the connection to Exchange
destinyConnection = ExchangeNTLMAuthConnection(url=destinyURL,
                                        username=destinyUsername,
                                        password=originPassword)

destinyService = Exchange2010Service(destinyConnection)

destinyCalendar = destinyService.calendar()

destinyEvents = destinyCalendar.list_events(
    start=timezone("America/Sao_Paulo").localize(datetime(2017, 11, 1, 0, 0, 0)),
    end=timezone("America/Sao_Paulo").localize(datetime(2017, 11, 17, 0, 0, 0)),
    details=True
)

print "Events from Origin Outlook"
originList = list()
for originEvent in originEvents.events:
    event = Event(originEvent.start, originEvent.end, originEvent.subject, originEvent.location, originEvent.html_body, originEvent.text_body, originEvent.attendees, originEvent.required_attendees, originEvent.optional_attendees, originEvent.recurrence, originEvent.recurrence_interval, originEvent.recurrence_end_date, originEvent.recurrence_days)
    originList.append(event);
    print "{start} {end} - {subject}".format(
        start=originEvent.start,
        end=originEvent.end,
        subject=originEvent.subject
    )  
print len(originList)
originList.sort

print "Events from Destiny Outlook"
destinyList = list()
for destinyEvent in destinyEvents.events:
    event = Event(destinyEvent.start, destinyEvent.end, destinyEvent.subject, destinyEvent.location, destinyEvent.html_body, destinyEvent.text_body, destinyEvent.attendees, destinyEvent.required_attendees, destinyEvent.optional_attendees, destinyEvent.recurrence, destinyEvent.recurrence_interval, destinyEvent.recurrence_end_date, destinyEvent.recurrence_days)
    destinyList.append(event);
    print "{start} {end} - {subject}".format(
        start=destinyEvent.start,
        end=destinyEvent.end,
        subject=destinyEvent.subject
    )  
print len(destinyList)

print "To include in Destiny"
for event in originList:
    if event not in destinyList:
        event = destinyService.calendar().new_event(
            subject=originEvent.subject,
            start=originEvent.start,
            end=originEvent.end,
            location=originEvent.location,
            html_body = originEvent.html_body,
            text_body = originEvent.text_body,
            recurrence = originEvent.recurrence,
            recurrence_interval = originEvent.recurrence_interval,
            recurrence_end_date = originEvent.recurrence_end_date,
            recurrence_days = originEvent.recurrence_days
        )
        event.create()


print "To include in Origin"
for event in destinyList:
    if event not in originList:
         event = originService.calendar().new_event(
            subject=destinyEvent.subject,
            start=destinyEvent.start,
            end=destinyEvent.end,
            location=destinyEvent.location,
            html_body = destinyEvent.html_body,
            text_body = destinyEvent.text_body,
            recurrence = destinyEvent.recurrence,
            recurrence_interval = destinyEvent.recurrence_interval,
            recurrence_end_date = destinyEvent.recurrence_end_date,
            recurrence_days = destinyEvent.recurrence_days
        )
        event.create()
       