import cmath
import math
import matplotlib.pyplot as plt
from datetime import datetime
from decimal import Decimal


class CustomLine:
    def __init__(self,system,phase_spacing_sym,a1,b1,c1,no_sub_conductors,sub_cond_spacing,no_strands,d,
    length,model,resistance,freq,nom_volt,power_rec,pf):
        """

        Args:
            system ([type]): [description]
            phase_spacing_sym ([type]): [description]
            a1 ([type]): [description]
            b1 ([type]): [description]
            c1 ([type]): [description]
            no_sub_conductors ([type]): [description]
            sub_cond_spacing ([type]): [description]
            no_strands ([type]): [description]
            d ([type]): [description]
            length ([type]): [description]
            model ([type]): [description]
            resistance ([type]): [description]
            freq ([type]): [description]
            nom_volt ([type]): [description]
            power_rec ([type]): [description]
            pf ([type]): [description]
        """
        self.system = system
        self.phase_spacing_sym = phase_spacing_sym
        self.a1 = a1
        self.b1 = b1
        self.c1 = c1
        self.no_sub_conductors = no_sub_conductors
        self.sub_cond_spacing=sub_cond_spacing
        self.no_strands=no_strands
        self.d=d
        self.length=length
        self.model=model
        self.resistance=resistance
        self.freq=freq
        self.nom_volt=nom_volt
        self.power_rec=power_rec
        self.pf=pf
        
        
        
    def calculate_parameter(self, show_plot=False):
        """

        Args:
            show_plot (bool, optional): [description]. Defaults to False.
        """
        #Receiving End Voltage

        VR=self.nom_volt/math.sqrt(3)


        #Calculating radius---r
        a = 3
        b = -3
        c = 1-self.no_strands
        # calculate the discriminant
        di = (b ** 2) - (4 * a * c)

        # find two solutions
        sol1 = (-b - cmath.sqrt(di)) / (2 * a)
        sol2 = (-b + cmath.sqrt(di)) / (2 * a)

        if (sol1.real >= sol2.real):
            n = sol1.real
        else:
            n= sol2.real


        D=(2*n-1)*self.d
        r=D/2

    # Inductance---L

        if(self.self.system==1):
            if(self.no_sub_cunductors==2):
                h=math.pow(self.no_sub_cunductors,2)
                i=math.pow(self.phase_spacing_sym,6)/(math.pow(r,1)*math.exp(-1/4)*math.pow(self.sub_cond_spacing,1))
                q=math.pow(i,1/h)
                print(q)

            elif(self.no_sub_cunductors==3):
                h = math.pow(self.no_sub_cunductors, 2)
                i = math.pow(self.phase_spacing_sym, 6) / math.pow(r*math.pow(self.sub_cond_spacing,2)*math.exp(-1/4),3)
                q = math.pow(i, 1 / h)
                print(q)

            elif(self.no_sub_cunductors==4):
                h = math.pow(self.no_sub_cunductors, 2)
                i = math.pow(self.phase_spacing_sym, 6) / math.pow(r*math.pow(self.sub_cond_spacing,3)*math.exp(-1/4)*math.sqrt(2),4)
                q = math.pow(i, 1 / h)

            else:
                h = math.pow(self.no_sub_cunductors, 2)
                i = math.pow(self.phase_spacing_sym, 6) / math.pow(r*math.exp(-1 / 4) * math.pow(self.sub_cond_spacing, 5) * 6,6)
                q = math.pow(i, 1 / h)


        else:
            if(self.no_sub_cunductors==2):

                h=math.pow(self.a1*self.b1*self.c1,1/3)
                i=math.exp(-1/(4*self.no_sub_cunductors))*math.pow(r,1/self.no_sub_cunductors)*math.pow(self.sub_cond_spacing,1/self.no_sub_cunductors)
                q=h/i

            elif(self.no_sub_cunductors==3):
                h = math.pow(self.a1 * self.b1 * self.c1, 1 / 3)
                i = math.pow( r * math.pow(self.sub_cond_spacing, 2) * math.exp(-1 / 4), 1 / self.no_sub_cunductors)
                q = h / i


            elif(self.no_sub_cunductors==4):
                h = math.pow(self.a1 * self.b1 * self.c1, 1 / 3)
                i = math.pow(math.sqrt(2)*r*math.pow(self.sub_cond_spacing,3)*math.exp(-1/4),1/self.no_sub_cunductors)
                q = h / i

            else:
                h = math.pow(self.a1 * self.b1 * self.c1, 1 / 3)
                i = math.pow(6 * r * math.pow(self.sub_cond_spacing, 5) * math.exp(-1 / 4), 1 / self.no_sub_cunductors)
                q = h / i

            L=2*math.pow(10,-4)*math.log(q)


#Capacitance---Cap

            if(self.model==1):
                Cap=0

            else:

                if (self.self.system == 1):

                    if (self.no_sub_cunductors == 2):
                        h = math.pow(self.no_sub_cunductors, 2)
                        i = math.pow(self.phase_spacing_sym, 6) / (math.pow(r, 1)  * math.pow(self.sub_cond_spacing, 1))
                        q = math.pow(i, 1 / h)
                        print(q)

                    elif (self.no_sub_cunductors == 3):
                        h = math.pow(self.no_sub_cunductors, 2)
                        i = math.pow(self.phase_spacing_sym, 6) / math.pow(r * math.pow(self.sub_cond_spacing, 2) , 3)
                        q = math.pow(i, 1 / h)
                        print(q)

                    elif (self.no_sub_cunductors == 4):
                        h = math.pow(self.no_sub_cunductors, 2)
                        i = math.pow(self.phase_spacing_sym, 6) / math.pow(r * math.pow(self.sub_cond_spacing, 3) * math.sqrt(2), 4)
                        q = math.pow(i, 1 / h)

                    else:
                        h = math.pow(self.no_sub_cunductors, 2)
                        i = math.pow(self.phase_spacing_sym, 6) / math.pow(r * math.pow(self.sub_cond_spacing, 5) * 6, 6)
                        q = math.pow(i, 1 / h)


                else:
                    if (self.no_sub_cunductors == 2):

                        h = math.pow(self.a1 * self.b1 * self.c1, 1 / 3)
                        i = math.pow(r, 1 / self.no_sub_cunductors) * math.pow(self.sub_cond_spacing, 1 / self.no_sub_cunductors)
                        q = h / i

                    elif (self.no_sub_cunductors == 3):
                        h = math.pow(self.a1 * self.b1 * self.c1, 1 / 3)
                        i = math.pow(r * math.pow(self.sub_cond_spacing, 2), 1 / self.no_sub_cunductors)
                        q = h / i

                    elif (self.no_sub_cunductors == 4):
                        h = math.pow(self.a1 * self.b1 * self.c1, 1 / 3)
                        i = math.pow(math.sqrt(2) * r * math.pow(self.sub_cond_spacing, 3) , 1 / self.no_sub_cunductors)
                        q = h / i

                    else:
                        h = math.pow(self.a1 * self.b1 * self.c1, 1 / 3)
                        i = math.pow(6 * r * math.pow(self.sub_cond_spacing, 5) , 1 / self.no_sub_cunductors)
                        q = h / i

                Cap = 2 * math.pi * 8.84 * math.pow(10, -9) / math.log(q)


    # Inductive Reactance---XL

        XL = 2 * math.pi * self.freq * L * self.length

    #Capacitive Reactance---XC
        if(self.model==1):
            XC= "infinite"
        else:
            XC=1/(2*math.pi*self.freq*Cap*self.length)

    # ABCD paramters

        if(self.model==1):
            Y=0
        else:
            Y=complex(0,1/XC)


        Z=complex(self.resistance*self.length,XL)

        if(self.model == 1):
            A = 1
            B = Z
            C = Y
            D = 1

        elif(self.model == 2):
            A = 1 + Y * Z / 2
            B = Z
            C = Y * (1 + Y * Z / 4)
            D = 1 + Y * Z / 2

        else:
            A = cmath.cosh(cmath.sqrt(Y * Z))
            B = cmath.sqrt(Z / Y) * cmath.sinh(cmath.sqrt(Y * Z))
            C = cmath.sqrt(Y / Z) * cmath.sinh(cmath.sqrt(Y * Z))
            D = cmath.cosh(cmath.sqrt(Y * Z))


    # Sending end line voltage---VS

        # Receving end current---IR

        IR = self.power_rec * math.pow(10, 6) / (self.pf * VR * 3)

        VS = (A*VR + IR*B)

    #charging current---IC

        if(self.model==1):
            IC=0

        elif(self.model==2):
            IC1=VS*Y/2
            IC2=VR*Y/2
            IC=IC1+IC2
        else:
            IC=C*VR

    # Sending end line Current----IS

        IS=C*VR + D*IR

    #Voltage Regulation---volt_reg

        if(self.model==1):
            volt_reg= (abs(VS)-abs(VR))*100/abs(VR)

        else:
            volt_reg= (abs(VS/A) -abs(VR))*100/abs(VR)


    #Power loss---power_loss

        power_loss = 3 * IR.real * IR.real * self.resistance * self.length

    #Transmission Efficiency---eff

        eff=self.power_rec*100/(self.power_rec+power_loss*math.pow(10,-6))

    #Angles

        angle_1=cmath.phase(A) #alpha
        angle_2=cmath.phase(B) #beta

        if show_plot:

            # Sending end circle

            x= -abs(A)*abs(VS/1000)*abs(VS/1000)*math.cos(angle_2-angle_1)/abs(B)
            y=abs(A)*abs(VS/1000)*abs(VS/1000)*math.sin(angle_2-angle_1)/abs(B)
            rad_1=abs(VS/1000)*abs(VR/1000)/abs(B)
            centre_1 = complex(x, y)
            fig, ax = plt.subplots()
            ax.set(xlim=(-5*rad_1, 5*rad_1), ylim=(-5*rad_1, 5*rad_1))
            a_circle = plt.Circle((x, y), rad_1)
            ax.add_artist(a_circle)
            plt.title('Sending End Circle', fontsize=12)
            plt.ylabel("Apparent Power")
            plt.xlabel("Real Power")
            plt.text(100, 200, 'Centre= %s\n Radius = %s\n' % (
                "{:g}".format(centre_1), "{:.3f}".format(rad_1)))


            #Receving end circle

            x1 = -abs(A) * abs(VR/1000) * abs(VR/1000) * math.cos(angle_2 - angle_1) / abs(B)
            y1 = -abs(A) * abs(VR/1000) * abs(VR/1000) * math.sin(angle_2 - angle_1) / abs(B)
            rad_2= abs(VS/1000) * abs(VR/1000) / abs(B)
            centre_2 = complex(x1, y1)
            fig, ax_1 = plt.subplots()
            ax_1.set(xlim=(-5*rad_2,5*rad_2), ylim=(-5*rad_2,5*rad_2))
            b_circle = plt.Circle((x1,y1), rad_2,color='r')
            ax_1.add_artist(b_circle)
            plt.title('Receving End Circle', fontsize=12)
            plt.ylabel("Apparent Power")
            plt.xlabel("Real Power")
            plt.text(100, 200, 'Centre= %s\n Radius = %s\n' % (
            "{:g}".format(centre_2),"{:.3f}".format(rad_2)))
            plt.show()
        
        features = {
        "Inductance": L,
        "Capacitance":Cap,
        "XL":XL,
        "XC":XC,
        "IC":IC,
        "A":A,
        "B":B,
        "C":C,
        "D":D,
        "VS":VS,
        "IS":IS,
        "volt_reg":volt_reg,
        "power_loss":power_loss,
        "eff":eff,
        "centre_1":centre_1,
        "rad_1":rad_1,
        "centre_2":centre_2,
        "rad_2":rad_2,
        "model":self.model
        }

        return features
        
