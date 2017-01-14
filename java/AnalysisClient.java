package com.julian.apps;

import com.google.appengine.api.datastore.DatastoreService;
import com.google.appengine.api.datastore.DatastoreServiceFactory;
import com.google.appengine.api.datastore.Entity;
import com.google.appengine.api.datastore.FetchOptions;
import com.google.appengine.api.datastore.Key;
import com.google.appengine.api.datastore.PreparedQuery;
import com.google.appengine.api.datastore.Query;
import com.google.appengine.tools.remoteapi.RemoteApiInstaller;
import com.google.appengine.tools.remoteapi.RemoteApiOptions;



import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.LinkedList;
import java.util.List;
import java.util.TimeZone;
import java.util.Vector;
import java.util.logging.Logger;




public class AnalysisClient {
	private static final Logger log = Logger.getLogger(AnalysisClient.class.getName());
	
	private static final int MAX_CLIENTS_RETRIEVE = 10000;
	private static final int CHUNKSIZE_CLIENTS = MAX_CLIENTS_RETRIEVE;	 
	private static final int MAX_PICKS_RETRIEVE = 10000;
	private static final int CHUNKSIZE_PICKS = MAX_PICKS_RETRIEVE;	 
	/**
	 * @param args
	 */

    public static void main(String[] args) throws IOException {
   	
		        String username = args[0];
		        String password = args[1];
		        RemoteApiOptions options = new RemoteApiOptions()
		            .server("seismocs.appspot.com", 443)
		            .credentials(username, password);
		        RemoteApiInstaller installer = new RemoteApiInstaller();
		        installer.install(options);
		        
				PrintWriter outFileClients = new PrintWriter(new FileWriter("MayClients.txt"));
				PrintWriter outFilePicks = new PrintWriter(new FileWriter("MayPicks.txt"));
				
				SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy MM dd HH:mm:ss.SSS zzz");
				dateFormat.setTimeZone(TimeZone.getTimeZone("UTC"));
				
				Vector phidgetIds = new Vector();
		        
		        DatastoreService ds;
		        try {
		            ds = DatastoreServiceFactory.getDatastoreService();

					
					// First get all clients
					Query q = new Query("ClientWithId");
					
					PreparedQuery pq = ds.prepare(q);
					FetchOptions limit = FetchOptions.Builder.withLimit(MAX_CLIENTS_RETRIEVE);
					limit.chunkSize(CHUNKSIZE_CLIENTS);

				
					List<Entity> entities = pq.asList(limit);
				
					int nPhidgets = 0;
					if (entities.size() == 0)
						System.out.println("No entities of type ClientWithId found");
					else {
						System.out.println("Got " + entities.size() + " ClientWithId objects");
						outFileClients.println("ID \tLocation \tName \tsensorType \tlastHeartbeat");
						for (Entity entity : entities) {
							Key key = entity.getKey();
							long id = key.getId();
							String sensorType = (String) entity.getProperty("sensorType");
							if(sensorType == null) continue;
							if(!sensorType.contains("Phidget")) continue;
							nPhidgets++;
							phidgetIds.add(id);
							outFileClients.println(id+"\t"+entity.getProperty("location")+"\t"+entity.getProperty("name")+"\t"+entity.getProperty("sensorType")+"\t"+entity.getProperty("lastHeartbeat"));
						}
					}
					System.out.println("A total of "+nPhidgets+" Phidget sensors");
								
					
					outFilePicks.println("pickDate \tClientId \tampX \tampY \tampZ \tLocation \treceiptDate");
					
					// NB all dates should be set in UTC !
		            // Yucaipa event 4.1 September
					//gc.set(2011, 8, 14, 14, 44, 51);
		            // Newhall event 4.2 September
		            //gc.set(2011, 8, 1, 20, 47, 07);
					// Saugas event 3.3 at 9/15/2011 18:23:25
					// gc.set(2011, 8, 25, 18, 22);
					
										
					//Calendar gc = GregorianCalendar.getInstance();
					Calendar gc = Calendar.getInstance(TimeZone.getTimeZone("UTC"));
					Calendar gcutil = Calendar.getInstance(TimeZone.getTimeZone("UTC"));
					
					// nb month is zero based
					gc.set(2012, 4, 1, 00, 00, 00);
					
					int numdays = 37;
					
					int houradd = 4;
					
					for(int ihour=0;ihour<24*numdays;ihour+=houradd) {
					
						
					//gc.add(Calendar.HOUR_OF_DAY, 8);
					//gc.add(Calendar.HOUR, -1);
					//gc.set(2011, 8, 25, 18, 21);
					Date dateAfterParam = gc.getTime();
					//gc.set(2011, 8, 1, 06, 00, 00);
					//gc.add(Calendar.HOUR, +1);
					gc.add(Calendar.HOUR, houradd);
					
					//gc.add(Calendar.MINUTE, 10);
					Date dateBeforeParam = gc.getTime();
					
					String beforeString = dateFormat.format(dateBeforeParam);
					String afterString = dateFormat.format(dateAfterParam);
					
					System.out.println("Using " + afterString + " as the start time.");										
					System.out.println("Using " + beforeString + " as the end time.");
		            	            
					q = new Query("Pick")
					.addFilter("receiptDate",  Query.FilterOperator.GREATER_THAN_OR_EQUAL, dateAfterParam);					
					q.addFilter("receiptDate", Query.FilterOperator.LESS_THAN_OR_EQUAL, dateBeforeParam);
				
					pq = ds.prepare(q);
					limit = FetchOptions.Builder.withLimit(MAX_PICKS_RETRIEVE);
					limit.chunkSize(CHUNKSIZE_PICKS);
				
					entities = pq.asList(limit);
				
					int nPhidgetPicks = 0;
					if (entities.size() == 0)
						System.out.println("No entities of type Pick found between "+dateAfterParam+" and "+dateBeforeParam);
					else {
						System.out.println("Got " + entities.size() + " Pick objects between "+afterString+" and "+beforeString);
						//List<Key> keys = new LinkedList<Key>();
						for (Entity entity : entities) {
							//System.out.println("Receipt Date "+entity.getProperty("receiptDate"));
							Long id = (Long)entity.getProperty("client");
							long clientId = id.longValue();
							if(!phidgetIds.contains(clientId)) continue;
							nPhidgetPicks++;
							Date d = (Date) entity.getProperty("receiptDate");						
							String rDate = dateFormat.format(d);
														
							d = (Date) entity.getProperty("pickDate");
							String pDate = dateFormat.format(d);
							
							outFilePicks.println(pDate+"\t"+clientId+"\t"+
									entity.getProperty("amplitudeX")+"\t"+
									entity.getProperty("amplitudeY")+"\t"+
									entity.getProperty("amplitudeZ")+"\t"+
									entity.getProperty("location")+"\t"+rDate);
						}
						System.out.println("A total of "+nPhidgetPicks+" Phidget picks");
					}
					
					}
		            
		            
		        } finally {
		        	System.out.println("Finished");
		        	outFileClients.close();
		        	outFilePicks.close();
		            installer.uninstall();
		        }
    }
}
