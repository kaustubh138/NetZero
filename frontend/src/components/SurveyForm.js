import { Component } from 'react';
import { FormOwnerInstituteInfo, FormOwnerPersonalInfo } from './FormOwnerInfo'
import FormVehicleInfo from './FormVehicleInfo'
import Success from './Success'

export class SurveyForm extends Component {
    #m_State = {
        step: 1,
        name: '',
        email: '',
        college: '',
        vehicle: '',
        license_plate: ''
    };

    nextStep = () => {
        const { step } = this.#m_State;
        this.setState({
            step: step + 1
        });
    };

    prevStep = () => {
        const { step } = this.#m_State;
        this.setState({
            step: step - 1
        });
    };

    handleChange = input => e => {
        this.setState({
            [input]: e.target.value
        });
    };

    render() {
        const { step, name, email, college, vehicle, license_plate } = this.#m_State;
        const values = { name, email, college, vehicle, license_plate };

        switch (step) {
            case 1:
                return (
                    <FormOwnerPersonalInfo
                        nextStep={this.nextStep}
                        handleChange={this.handleChange}
                        value={values} />
                );
            case 2:
                return (
                    <FormOwnerInstituteInfo />
                );
            case 3:
                return (
                    <FormVehicleInfo />
                );

            case 4:
                return <Success />;
            default:
                console("NetZero: A Sustainable Future")
        }

        return;
    }
}

export default SurveyForm;