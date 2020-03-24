//电机驱动相关参数，使用L298N电机驱动模块
#define PIN_PWML 3//左轮pwm控制，连驱动板ENA
#define PIN_INL1 2//控制左轮的引脚1，连驱动板的IN1
#define PIN_INL2 4//控制左轮的引脚2，连驱动板的IN2
#define PIN_PWMR 5//右轮pwm控制，连驱动板ENB
#define PIN_INR1 7//控制右轮的引脚1，连驱动板的IN3
#define PIN_INR2 8//控制右轮的引脚2，连驱动板的IN4
//循迹引脚定义
#define PIN_TRACE_1 9;//左边的循迹模块（可自己用二极管和光敏三极管做）
#define PIN_TRACE_2 10;//中间的循迹模块
#define PIN_TRACE_3 11;//右边的循迹模块

void motor_start() {
  digitalWrite(PIN_INL1,HIGH);
  digitalWrite(PIN_INL2,LOW);
  digitalWrite(PIN_INR1,HIGH);
  digitalWrite(PIN_INR2,LOW);
  analogWrite(PIN_PWMl,255);
  analogWrite(PIN_PWMR,255);
}

void turn_left() {
  analogWrite(PIN_PWMl,50);
  //转弯怎么转还没确定
}

void turn_right() {
  analogWrite(PIN_PWMR,50);
}

void recover_straight () {
  //如果性能不够，撤掉函数
  analogWrite(PIN_PWMl,255);
  analogWrite(PIN_PWMm,255);
}

void setup() {
  //电机初始化引脚设置
  pinMode(PIN_PWML,OUTPUT);
  pinMode(PIN_INL1,OUTPUT);
  pinMode(PIN_INL2,OUTPUT);
  pinMode(PIN_PWMR,OUTPUT);
  pinMode(PIN_INR1,OUTPUT);
  pinMode(PIN_INR2,OUTPUT);
  //循迹引脚设置
  pinMode(PIN_TRACE_1,INPUT);
  pinMode(PIN_TRACE_2,INPUT);
  pinMode(PIN_TRACE_3,INPUT);
  // 起步延迟10s
  delay(10000);
  motor_start();
}

void loop() {
  //循迹程序，如果效果不好可采用PID调节，可参考文档中的链接
  int trace_data1 = digitalRead(PIN_TRACE_1);
  int trace_data2 = digitalRead(PIN_TRACE_2);
  int trace_date3 = digitalRead(PIN_TRACE_3);
  if(!trace_data1 & trace_data2 & !trace_data3) {
    recover_straight();
  }
  else if(trace_data1 & trace_data2 & !trace_data3) {
    turn_left();
  }
  else if(!trace_data1 & trace_data2 & trace_data3) {
    turn_right();
  }
}
