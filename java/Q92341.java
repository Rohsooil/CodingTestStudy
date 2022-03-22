import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Q92341 {

    static final String IN = "IN";
    static final String OUT = "OUT";
    static final String LAST_TIME = "23:59";

    class Car {

        String number;
        String time;
        String status;
        int accumulatedMinutes;

        Car(String number, String time) {
            this.number = number;
            this.time = time;
            this.status = OUT;
            this.accumulatedMinutes = 0;
        }
    }

    public int[] solution(int[] fees, String[] records) {
        int baseMinutes = fees[0];
        int baseFee = fees[1];
        int unitMinutes = fees[2];
        int unitFee = fees[3];

        Map<String, Car> carMap = new HashMap<>();

        for (String record : records) {

            String[] splited = record.split(" ");
            String carNumber = splited[1];
            String time = splited[0];
            String status = splited[2];

            Car car = carMap.getOrDefault(carNumber, new Car(carNumber, time));
            if (car.status.equals(IN)) {
                car.accumulatedMinutes += calculatesInOut(car.time, time);
            }
            car.time = time;
            car.status = status;
            carMap.put(carNumber, car);
        }

        return carMap.keySet().stream().sorted()
                .mapToInt(key -> calculatesFee(baseMinutes, baseFee, unitMinutes, unitFee, carMap.get(key))).toArray();
    }

    private int calculatesInOut(String in, String out) {

        return toMinutes(out) - toMinutes(in);
    }

    private int toMinutes(String time) {
        String[] timeArr = time.split(":");
        return Integer.valueOf(timeArr[0]) * 60 + Integer.valueOf(timeArr[1]);
    }

    private int calculatesFee(int baseMinutes, int baseFee, int unitMinutes, int unitFee, Car car) {

        if (car.status.equals(IN)) {
            car.accumulatedMinutes += calculatesInOut(car.time, LAST_TIME);
        }

        if (car.accumulatedMinutes <= baseMinutes) {
            return baseFee;
        }

        return baseFee + roundUpMinutes(car.accumulatedMinutes, baseMinutes, unitMinutes) * unitFee;
    }

    private int roundUpMinutes(int accumulatedMinutes, int baseMinutes, int unitMinutes) {
        if ((accumulatedMinutes - baseMinutes) % unitMinutes == 0) {
            return (accumulatedMinutes - baseMinutes) / unitMinutes;
        }
        return (accumulatedMinutes - baseMinutes) / unitMinutes + 1;
    }

    public static void main(String[] args) {
        Arrays.stream(new Q92341().solution(new int[]{180, 5000, 10, 600},
                new String[]{"05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN",
                        "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"})).forEach(System.out::println);
        Arrays.stream(new Q92341().solution(new int[]{120, 0, 60, 591},
                new String[]{"16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"})).forEach(System.out::println);
    }

}
